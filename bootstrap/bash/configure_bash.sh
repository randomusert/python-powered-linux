#!/bin/bash
set -e

echo "Configuring bash source"

cd bash-5.3
export BUILD_DIR=$(pwd)/build

if [ ! -d "$BUILD_DIR" ]; then
    echo "Creating build directory at: $BUILD_DIR"
    mkdir -p "$BUILD_DIR"
else
    echo "Build directory already exists at: $BUILD_DIR. continuing with existing directory."
fi

cd build

../configure --prefix=/usr/bin


echo "Bash configured successfully"