add_subdirectory(union)
add_subdirectory(intrusive_ptr)

target_link_libraries(${CMAKE_PROJECT_NAME}
	PRIVATE
		union
		crimson_cell::intrusive_ptr
)

target_include_directories(${CMAKE_PROJECT_NAME}
	PRIVATE
		"."
)