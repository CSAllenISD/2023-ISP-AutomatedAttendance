cmake_minimum_required(VERSION 3.0)

project(YourProjectName)

# Add sources and headers to the project
set(SOURCES
    src/main.cpp
    src/other_file.cpp
)

set(HEADERS
    include/your_header.hpp
    include/other_header.hpp
)

# Define the target
add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})

# Set include directories
target_include_directories(${PROJECT_NAME} PRIVATE include)

# Set C++ standard to C++11
set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 11)

# Link external libraries if needed
target_link_libraries(${PROJECT_NAME} PRIVATE your_library_name)

# Set output directory for the executable
set_target_properties(${PROJECT_NAME} PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)

# Add a custom command for copying resources to the output directory
add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_SOURCE_DIR}/resources ${CMAKE_BINARY_DIR}/bin/resources
)
