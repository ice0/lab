cmake_minimum_required(VERSION 3.21)
project(gtkmm)

set(CMAKE_CXX_STANDARD 11)

find_package(PkgConfig)
pkg_check_modules(GTKMM REQUIRED gtkmm-3.0)

add_executable(gtkmm main.cpp examplewindow.h examplewindow.cpp)
target_compile_options(gtkmm PRIVATE ${GTKMM_CFLAGS})
target_link_libraries(gtkmm ${GTKMM_LDFLAGS})
