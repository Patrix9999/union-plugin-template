# Introduction

This project serves as a starting point for creating a union plugin for the following Gothic games:
- [Gothic I](https://gothic.fandom.com/wiki/Gothic_1)
- [Gothic Sequel](https://gothic.fandom.com/wiki/Gothic_Sequel)
- [Gothic II](https://en.wikipedia.org/wiki/Gothic_II)
- [Gothic II Night of The Raven](https://en.wikipedia.org/wiki/Gothic_II:_Night_of_the_Raven).

It provides a preconfigured base code designed to simplify the development process and help you focus on building new features for your plugin.

# Requirements

Before you start making your own plugin, you need to install some software first, here's a full list of things that you'll need to install to be able to build the union plugin:
- [git](https://git-scm.com/) **Required** for version control and to clone the project repository
- [CMake](https://cmake.org/) **Required** for command-line and Linux builds; optional when using Visual Studio's bundled CMake
- [Visual Studio](https://visualstudio.microsoft.com/pl/) **Required on Windows** for compiling the plugin using the MSVC toolset
	(make sure to install **C++ Workload** and **CMake Tools for Visual Studio**)

Linux builds additionally require:
- [mstorsjo/msvc-wine](https://github.com/mstorsjo/msvc-wine) with the x86 MSVC and Windows SDK files installed
- [Ninja](https://ninja-build.org/)
- [Wine](https://www.winehq.org/)
- Clang/`clang-cl` for VS Code IntelliSense

The Union plugin still uses the real MSVC toolset on Linux through msvc-wine.
Alternative toolchains such as MinGW are not used.

# Fetching the source code

1. Make sure to clone the your project repository recursively (to fetch all of the [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)).  
2. You can achieve this by typing this command in your terminal: 
```git 
git clone --recursive URL_TO_YOUR_REPO
```

# Configuration

The plugin template contains special file called `CMakeUserConfigPresets.json`  
in which you can manully specify the variables for your own needs.  

Linux users should set the root of their msvc-wine installation in the
`msvc-wine-config` preset:

```json
{
  "name": "msvc-wine-config",
  "hidden": true,
  "cacheVariables": {
    "MSVC_WINE_ROOT": "$env{HOME}/my_msvc/opt/msvc"
  }
}
```

Change only the value when msvc-wine is installed elsewhere. Use an absolute
path or `$env{HOME}`; CMake presets do not expand `~`. The selected directory
must contain `bin/x86`, `VC/Tools/MSVC`, and `Windows Kits/10`.

**NOTE!** By default this file is tracked via git, but it shouldn't be, to not track it,  
type this command in root repo dir:  
```bash
git update-index --assume-unchanged CMakeUserConfigPresets.json
```

Core plugin configuration is located in **REPO_ROOT/CMakeLists.txt**.  
Some of the common things that you should propably change are:
- **project name** (this is also setting the name of your plugin dll)  
	default value is **UnionPlugin**
- **project version**  
	default value is **1.0.0.0**

# Building on Windows

Follow the steps below to compile the plugin:

## Step 1: Open the Project in Visual Studio

1. Navigate to the root directory of your repository.
2. Right-click on the folder's content (without selecting any files or subfolders).
3. Select **Open with Visual Studio** from the context menu.

## Step 2: Choose a Configuration

1. In Visual Studio, locate the Solution Configurations dropdown menu in the top toolbar.
2. Select the desired configuration for your build

## Step 3: Pick the Startup Project

1. In Visual Studio, locate the Solution Startup Item dropdown menu in the top toolbar.
2. Select your plugin from dropdown list

### Step 4: Build the plugin

1. Once everything is configured, click **Build Solution** (or press **Ctrl+Shift+B**).
2. If you've configured everything correctly, the build process should complete successfully.

# Building on Linux

After installing msvc-wine and setting `MSVC_WINE_ROOT`, configure and build
the preset matching the desired game and build type:

```bash
cmake --fresh --preset G2A-Release-msvc-wine
cmake --build --preset G2A-Release-msvc-wine
```

Available Linux presets follow the same `G1`, `G1A`, `G2`, `G2A`, and `MP`
plus `Debug` or `Release` naming as the Windows presets, with
`-msvc-wine` appended. For example:

```text
G1-Debug-msvc-wine
G1-Release-msvc-wine
G2A-Release-msvc-wine
MP-Release-msvc-wine
```

Use MP only when the plugin supports all four engines. The Linux build creates
a 32-bit Windows DLL and packages the VDF in `out/build/PRESET_NAME/vdf/`.
`GothicVDFS.exe` runs through Wine automatically on Linux.

## VS Code IntelliSense on Linux

The repository includes configurations for Microsoft C/C++ and clangd.
Configuring a Linux preset generates `compile_commands.json` and selects that
preset for IntelliSense automatically. The current `.ipp` sources receive
editor-only compilation entries with the matching Gothic engine context;
these entries do not add objects to normal plugin builds.

The C/C++ extension automatically selects the `Linux` configuration on Linux
and the `Win32` configuration on Windows. Windows uses the CMake Tools
configuration provider instead of the Linux compilation database. A root
symlink left by Linux is harmless on Windows and remains available when the
workspace is opened on Linux again.

After configuring for the first time or changing presets, run
**C/C++: Reset IntelliSense Database** and **Developer: Reload Window** in VS
Code. Open `src/Plugin.ipp` and run **C/C++: Log Diagnostics** to verify that
the active translation unit contains the MSVC, Windows SDK, Gothic API, and
Union API include paths.

# Plugin installation

Once the plugin has been compiled successfully, you can tell the game to load it during startup by placing it in `Game/System/autorun` subdirectory.  

To do that copy the plugin:  
**from**: `REPO_ROOT/out/build/YOUR_CONFIGURATION/YOUR_PROJECT_NAME.dll`  
**to**: `GAME_ROOT/System/autorun/`

You also need to copy `UnionAPI.dll` into `Game/System`.

You can also create a symbolic link for your dll in `Game/System/autorun` subdirectory, that way you won't be forced to copy the plugin dll each time while you compile a new version of your plugin.  
On Windows you can use [Link Shell Extension](https://schinagl.priv.at/nt/hardlinkshellext/linkshellextension.html) that allows you to create symlinks from file context menu.

Alternatively you can just copy `UnionPlugin.vdf` into `Game/Data` directory.  
This will work, because `UnionPlugin.vdf` already constains `UnionAPI.dll` inside of it.

# Publishing plugin

This project provides [github action](https://github.com/features/actions) for compiling and releasing a new version of your plugin via github.  

Before you publish a new release, make sure to set a new version in **CMakeLists.txt**, and document your changes in **CHANGELOG.md** file. I recommend updating your changelog file regularly during the development of your plugin, to not forget about adding this later.

To publish a new version of your plugin you just need to create a new [github release](https://github.com/Patrix9999/union-plugin-template/releases).  
**YOU MUST NAME YOUR RELEASE** using following versioning schema: `major.minor.[patch].[tweak]`, e.g: `1.0`.  
Alternatively you can also trigger the pipeline manually, this can be useful for beta versions of your plugins.

And that's it, when plugin will be built successfully it will automatically be added as release asset to the newest release. By default CI/CD script is using the **MP-Release** configuration, depending on your plugin requirements you might want to change this, to match your plugin supported platform(s).
