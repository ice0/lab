#!/usr/bin/env bash
# -------------------------------------------------------------------------------
# This script builds mlt++ required by synfig-core
# -------------------------------------------------------------------------------
set -e # exit on error

mkdir build
cd build
cmake ../cpp -GNinja
ninja
./main