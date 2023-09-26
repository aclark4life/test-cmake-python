cmake_minimum_required(VERSION 3.12)
project(hello_world_cpp)

# Set C++ standard to C++11
set(CMAKE_CXX_STANDARD 11)

# Build the shared library
add_library(hello SHARED hello_world.cpp)

# Provide a name for the Python module
set_target_properties(hello PROPERTIES PREFIX "" OUTPUT_NAME "hello")

# Find Python
find_package(Python REQUIRED)
include_directories(${Python_INCLUDE_DIRS})

# Link the shared library with Python
target_link_libraries(hello ${Python_LIBRARIES})
