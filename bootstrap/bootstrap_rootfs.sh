#!/bin/bash
set -e
set -u
set -o pipefail

build_glibc() {
    wget https://ftp.gnu.org/gnu/glibc/glibc-2.44.tar.gz
    tar -xf glibc-2.44.tar.gz
    cd glibc-2.44
    mkdir build
    cd build
    ../configure --prefix=/usr
    make -j$(nproc)
    echo "Run make DESTDIR=/path/to/rootfs install to install glibc to the root filesystem"
}

build_bash() {
    echo "Fetching bash source archive from ftp.gnu.org"

    wget https://ftp.gnu.org/gnu/bash/bash-5.3.tar.gz

    echo "Extracting bash source archive"

    tar -xf bash-5.3.tar.gz

    echo "Bash source fetched and extracted successfully"

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

    echo "Building bash source"

    make -j$(nproc)

    echo "Bash built successfully"
}

build_busybox() {
    echo "TODO: Implement BusyBox build process"
}

build_libs() {
    echo "LIBS list: ncurses, openSSL, kernel headers"
}