cmake_minimum_required(VERSION 3.12)

# define build/lib/include/bin dirs and cmake module dir
include(cmake/environment.cmake)

project(QuantExtBoilerplate CXX)

# default C++ arguments.
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -std=c++11")

add_subdirectory(lib)
add_subdirectory(src)
