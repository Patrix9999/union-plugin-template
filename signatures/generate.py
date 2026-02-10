import idautils
import idc
import idaapi
import re
import os
import ctypes

# Demangler

dbghelp = ctypes.WinDLL("dbghelp")

UnDecorateSymbolName = dbghelp.UnDecorateSymbolName
UnDecorateSymbolName.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint]
UnDecorateSymbolName.restype = ctypes.c_uint

def demangle(name: str) -> str:
    buf = ctypes.create_string_buffer(1024)
    UnDecorateSymbolName(name.encode(), buf, len(buf), 0)
    return buf.value.decode()

# Class signature matching

pattern = re.compile(
    r"""
    ^(?:(?:public|private|protected):\s+)?                                  # optional access specifier
    (?:static\s+)?                                                          # optional 'static'
    (?:virtual\s+)?                                                         # optional 'virtual'
    (?:(?P<return>[\w\s:<>,*&]+?)\s+)?                                      # optional return type
    (?P<callconv>__thiscall|__cdecl|__stdcall|__fastcall|__vectorcall)\s+   # optional calling convention  
    (?:(?P<class>[\w:<>]+)::)?                                              # optional class name (allow nested/templates)
    (?P<method>.+?)\s*                                                      # method name or operator overload
    \((?P<args>.*)\).*$                                                     # argument list
    """,
    re.VERBOSE
)

def parse_signature(signature: str) -> dict:
    """Parse a C++-style function signature into structured components."""
    match = pattern.match(signature)
    if not match:
        return None

    return_type = match.group("return")
    callconv = match.group("callconv")
    class_name = match.group("class") or ""
    method_name = match.group("method")
    args_raw = match.group("args").strip()

    if args_raw == "void" or args_raw == "":
        args = []
    else:
        args = [arg.strip() for arg in args_raw.split(",") if arg.strip()]

    if return_type is None or return_type == "":
        if method_name == class_name:
            return_type = f"{class_name}*"
        else:
            return_type = "void"

    return {
        "return_type": return_type,
        "calling_convention": callconv,
        "class_name": class_name,
        "method_name": method_name,
        "arguments": args,
    }

# Signature file generation

project_path = idaapi.get_input_file_path()
project_name = os.path.splitext(os.path.basename(project_path))[0]

output_file = f"{project_name}_signatures.hpp"

gothic_namespaces = {
    "g1": "Gothic_I_Classic",
    "g1a": "Gothic_I_Addon",
    "g2": "Gothic_II_Classic",
    "g2a": "Gothic_II_Addon",
}

signatures = {}

for func_ea, name in idautils.Names():
    if not idc.is_code(idc.get_full_flags(func_ea)):
        continue

    raw_name = idc.get_func_name(func_ea)
    if not raw_name:
        raw_name = name

    demangled_name = demangle(raw_name)

    try:
        signature = parse_signature(demangled_name)
        if signature is None:
            #print(f"skipped: {demangled_name}")
            continue

        signature_key = f"{signature['class_name']}::{signature['method_name']}" if signature['class_name'] else signature['method_name']
        if signature_key in signatures:
            #print(f"skipped duplicate: {signature_key} 0x{func_ea:x}")
            continue

        signatures[signature_key] = func_ea

    except Exception as e:
        print(f"Exception occurred: {e}")
        continue

with open(output_file, "w") as f:
    f.write("#pragma once\n\n")
    f.write("#include <cstdint>\n")
    f.write("#include <string_view>\n\n")

    f.write(f"namespace {gothic_namespaces[project_name]}\n")
    f.write(f"{{\n")
    f.write(f"\tstruct SignatureEntry\n")
    f.write(f"\t{{\n")
    f.write(f"\t\tstd::string_view signature;\n")
    f.write(f"\t\tstd::uint32_t address;\n")
    f.write(f"\t}};\n\n")

    f.write(f"\tconstexpr SignatureEntry signatures[] = {{\n")

    for key, value in signatures.items():
        f.write(f'\t\t{{ "{key}", 0x{value:X} }},\n')

    f.write("\t};\n\n")

    f.write(f"\tconsteval std::uint32_t SignatureToAddress(const std::string_view signature)\n")
    f.write(f"\t{{\n")
    f.write(f"\t\tfor (auto const& [entry_signature, entry_address] : signatures)\n")
    f.write(f"\t\t{{\n")
    f.write(f"\t\t\tif (entry_signature == signature)\n")
    f.write(f"\t\t\t\treturn entry_address;\n")
    f.write(f"\t\t}}\n\n")
    f.write(f"\t\treturn 0;\n\n")
    f.write(f"\t}}\n")
    f.write(f"}}")

print(f"Exported function list to {output_file}")