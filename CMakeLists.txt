cmake_minimum_required(VERSION 3.21)

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/")
set(CMAKE_POLICY_VERSION_MINIMUM 3.5)

set(PROJECT_VERSION "1.0.0.0" CACHE STRING "Project version")

include(target_add_versioninfo)

project(UnionPlugin
	DESCRIPTION "Union plugin for Gothic Games"
	VERSION ${PROJECT_VERSION}
)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# By default template uses dynamically linked union-api target to avoid compatibility problems.
# If you want to produce a standalone plugin, set this option to OFF
set(GENERATE_UNION_API_DLL ON)

file(GLOB_RECURSE SRC
    "src/*.cpp"
	"resources/*.h"
	"resources/*.rc"
)

add_library(${CMAKE_PROJECT_NAME} SHARED)
target_sources(${CMAKE_PROJECT_NAME} PRIVATE ${SRC})

target_include_directories(${CMAKE_PROJECT_NAME}
    INTERFACE
		"include/"

	PRIVATE
		BEFORE "userapi/"
		"src/"
		"resources/"
)

target_add_versioninfo(${CMAKE_PROJECT_NAME}
	VERSION "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.${PROJECT_VERSION_PATCH}.${PROJECT_VERSION_TWEAK}"
	COMPANY_NAME "Gothic Community"
	PRODUCT_NAME "${CMAKE_PROJECT_NAME}"
)

if (GENERATE_UNION_API_DLL)
	set(VDF_DIR "${PROJECT_SOURCE_DIR}/vdf/")
	set(VDF_AUTORUN_DIR "${VDF_DIR}System/Autorun/")

	set(VDF_BUILD_VM_FILE "${VDF_DIR}build.vm")
	string(REPLACE "/" "\\" VDF_BUILD_VM_FILE "${VDF_BUILD_VM_FILE}")

	add_custom_target(copy_union_api_dll
		ALL
			COMMAND ${CMAKE_COMMAND} -E make_directory ${VDF_AUTORUN_DIR}
			COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:union_api_dll> ${VDF_AUTORUN_DIR}
			COMMAND ${CMAKE_COMMAND} -E echo "[Post Build] $<TARGET_FILE_NAME:union_api_dll> copied to: ${VDF_AUTORUN_DIR}"
		DEPENDS union_api_dll
	)

	add_custom_command(TARGET ${CMAKE_PROJECT_NAME}
		POST_BUILD
			COMMAND ${CMAKE_COMMAND} -E make_directory ${VDF_AUTORUN_DIR}
			COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:${CMAKE_PROJECT_NAME}> ${VDF_AUTORUN_DIR}
			COMMAND ${CMAKE_COMMAND} -E echo "[Post Build] $<TARGET_FILE_NAME:${CMAKE_PROJECT_NAME}> copied to: ${VDF_AUTORUN_DIR}")

	add_custom_target(build_vdf
		ALL
			COMMAND ${CMAKE_COMMAND} -E echo "[VDF] Building ${CMAKE_PROJECT_NAME}.vdf ..."
			COMMAND "${VDF_DIR}/GothicVDFS.exe" /B "${VDF_BUILD_VM_FILE}"
			COMMAND ${CMAKE_COMMAND} -E rename "${VDF_DIR}/plugin.vdf" "${VDF_DIR}/${CMAKE_PROJECT_NAME}.vdf"
			COMMAND ${CMAKE_COMMAND} -E echo "[VDF] ${CMAKE_PROJECT_NAME}.vdf build successfully!"
		WORKING_DIRECTORY "${VDF_DIR}"
		DEPENDS ${CMAKE_PROJECT_NAME}
	)
endif()

add_subdirectory(dependencies)