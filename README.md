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
- [CMake](https://cmake.org/) **Optional** if you plan to use Visual Studio
- [Visual Studio](https://visualstudio.microsoft.com/pl/) **Essential** for compiling the plugin using the MSVC toolset  
	(make sure to install **C++ Workload** and **CMake Tools for Visual Studio**)

The Union plugin requires the MSVC toolset for compatibility, so alternative toolchains like MinGW are not supported.

# Fetching the source code

1. Make sure to clone the your project repository recursively (to fetch all of the [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)).  
2. You can achieve this by typing this command in your terminal: 
```git 
git clone --recursive URL_TO_YOUR_REPO
```

# Configuration

All of the plugin configuration is located in **REPO_ROOT/CMakeLists.txt**.  
Some of the common things that you should propably change are:
- **project name** (this is also setting the name of your plugin dll)  
	default value is **UnionPlugin**
- **project version**  
	default value is **1.0.0.0**

# Building

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

# Plugin installation

Once the plugin has been compiled successfully, you can tell the game to load it during startup by placing it in `System/autorun` subdirectory.

To do that copy the plugin:  
**from**: `REPO_ROOT/out/build/YOUR_CONFIGURATION/YOUR_PROJECT_NAME.dll`  
**to**: `GAME_ROOT/System/autorun/`

You can also create a symbolic link for your dll in `System/autorun` subdirectory, that way you won't be forced to copy the plugin dll each time while you compile a new version of your plugin.  
On Windows you can use [Link Shell Extension](https://schinagl.priv.at/nt/hardlinkshellext/linkshellextension.html) that allows you to create symlinks from file context menu.

# Publishing plugin

This project provides [github action](https://github.com/features/actions) and [gitlab pipeline](https://docs.gitlab.com/ci/yaml/) for compiling and releasing a new version of your plugin.  

Before you publish a new release, make sure to set a new version in **CMakeLists.txt**, and document your changes in **CHANGELOG.md** file. I recommend updating your changelog file regularly during the development of your plugin, to not forget about adding this later.

To publish a new version of your plugin you just need to create a new [github release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) or [gitlab release](https://docs.gitlab.com/user/project/releases/) or push a [git tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging).  
I recommend naming your release by using your plugin version.

And that's it, when plugin will be built successfully it will automatically be added as release asset to the newest release. By default CI/CD script is using the **MP-Release** configuration, depending on your plugin requirements you might want to change this, to match your plugin supported platform(s).