cmake_minimum_required(VERSION 3.25)

project("autocode templates" CXX)

find_package(Python3 COMPONENTS Interpreter REQUIRED)

set(CMAKE_CXX_STANDARD 17)

FILE(GLOB_RECURSE AUTOCODE_SRC ${CMAKE_CURRENT_SOURCE_DIR}/autocoder/*)

add_subdirectory(autocode_user)

add_executable(main main.cpp)

target_link_libraries(main automod)
