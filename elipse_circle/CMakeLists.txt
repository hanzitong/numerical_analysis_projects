
cmake_minimum_required(VERSION 3.8)
project(elipse_circle)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
  # add_compile_options(-Wall -Wextra -Wpedantic -v)
endif()

# find_package(iostream)  # this will fail
# find_package(nlopt)     # this also will fail

add_executable(calc_intersection example/main.cpp)
target_include_directories(calc_intersection PRIVATE include)
target_link_libraries(calc_intersection PRIVATE nlopt)

add_executable(gendata_objfunc_elipse_circle plot/gendata_objfunc_elipse_circle.cpp)
target_include_directories(gendata_objfunc_elipse_circle PRIVATE include)
target_link_libraries(calc_intersection PRIVATE nlopt)
install(TARGETS gendata_objfunc_elipse_circle DESTINATION ${CMAKE_SOURCE_DIR}/plot)


