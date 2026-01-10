import argparse
import re
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Tuple


pattern = re.compile(
    r"""
    ^(?:(?:public|private|protected):\s+)?          # optional access specifier
    (?:static\s+)?                                  # optional 'static'
    (?:virtual\s+)?                                 # optional 'virtual'
    (?:\[\s*thunk\s*\]:\s*)?                     # optional thunk prefix
    (?:(?P<return>.+?)\s+)?                         # optional return type (lazy up to callconv)
    (?P<callconv>__thiscall|__cdecl|__stdcall|__fastcall|__vectorcall)\s+
    (?:(?P<class>[\w:<>]+)::)?                      # optional class name
    (?P<method>[^(]+?)\s*                           # method name (non-paren, lazy)
    \((?P<args>(?:[^()]|\([^()]*\))*)\)\s*         # args: non-parens OR one level of nested parens
    (?P<qualifiers>const\s*volatile?|volatile\s*const|const)?\s*$  # optional cv-qualifiers
    """,
    re.VERBOSE,
)


def parse_signature(signature: str) -> Optional[dict]:
    """Parse a C++-style function signature into structured components."""
    match = pattern.match(signature)
    if not match:
        return None

    return_type = match.group("return")
    callconv = match.group("callconv")
    class_name = match.group("class") or ""
    method_name = match.group("method")
    qualifiers = (match.group("qualifiers") or "").strip()
    args_raw = match.group("args").strip()

    if args_raw in {"void", ""}:
        args = []
    else:
        args = [arg.strip() for arg in args_raw.split(",") if arg.strip()]

    if not return_type:
        return_type = f"{class_name}*" if method_name == class_name else "void"

    # Qualifiers like 'const' are parsed but omitted from output columns.

    return {
        "return_type": return_type,
        "calling_convention": callconv,
        "class_name": class_name,
        "method_name": method_name,
        "arguments": args,
    }


def normalize_signature(signature: str) -> str:
    """Strip noise that appears in Names.txt exports before parsing."""
    return signature.replace("[thunk]:", "").strip()


def convert_lines(lines: Iterable[str], warn: bool = False) -> Tuple[List[str], List[str]]:
    converted: List[str] = []
    skipped: List[str] = []

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue

        if " " not in line:
            if warn:
                skipped.append(line)
            continue

        address_text, signature_raw = line.split(" ", 1)

        try:
            address = hex(int(address_text, 16))
        except ValueError:
            if warn:
                skipped.append(line)
            continue

        signature = normalize_signature(signature_raw)
        parsed = parse_signature(signature)
        if not parsed:
            if warn:
                skipped.append(line)
            continue

        row = [
            address,
            parsed["return_type"],
            parsed["calling_convention"],
            parsed["class_name"],
            parsed["method_name"],
        ]

        if parsed["arguments"]:
            row.extend(parsed["arguments"])
        else:
            row.append("")

        converted.append("\t".join(row))

    return converted, skipped


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert Gothic Names.txt exports into Union signature format.",
    )
    parser.add_argument("input", help="Path to Names.txt form Gothic API")
    parser.add_argument(
        "-o",
        "--output",
        help="Output path (defaults to input basename with .txt)",
    )
    parser.add_argument(
        "--warnings",
        action="store_true",
        help="Print lines that could not be parsed",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 1

    output_path = (
        Path(args.output)
        if args.output
        else input_path.with_suffix(".txt")
    )

    lines = input_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    converted, skipped = convert_lines(lines, warn=args.warnings)

    output_path.write_text("\n".join(converted), encoding="utf-8")
    print(f"Wrote {len(converted)} entries to {output_path}")

    if args.warnings and skipped:
        print(f"Skipped {len(skipped)} line(s) that could not be parsed:", file=sys.stderr)
        for line in skipped:
            print(f"  {line}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())