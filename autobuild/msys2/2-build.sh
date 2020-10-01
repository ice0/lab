#!/usr/bin/env bash
# -------------------------------------------------------------------------------
# This script builds mlt++ required by synfig-core
# -------------------------------------------------------------------------------
set -e # exit on error

pacman -S ${MINGW_PACKAGE_PREFIX}-lld

mkdir -p build
cd build
cmake ../cpp -GNinja
ninja
./main