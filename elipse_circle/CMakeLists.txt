
cmake_minimum_required(VERSION 3.8)
project(elipse_circle)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
  # add_compile_options(-Wall -Wextra -Wpedantic -v)
endif()

# find_package(iostream)  # this will fail
# find_package(nlopt)     # this also will fail

add_executable(calc_intersection src/main.cpp)
target_include_directories(calc_intersection PRIVATE include)
target_link_libraries(calc_intersection PRIVATE nlopt)

