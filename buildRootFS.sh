#!/bin/sh
set -e
set -o pipefail


build_rootfs() {
    if [ ! -d "$TINOSPPLE_ROOTFS" ]; then
        echo "Error: TINOSPPLE_ROOTFS directory does not exist or the variable is not set."
        exit 1
    fi

    (
        cd "$TINOSPPLE_ROOTFS"
        find . -print0 | cpio --null -ov --format=newc
    ) | gzip -9 > "$HOME/tinospple_initrd.img"
}

while getopts "r:" opt; do
    case $opt in
        r)
            TINOSPPLE_ROOTFS="$OPTARG"
            ;;
        *)
            echo "Usage: $0 -r <path_to_tinospple_rootfs>"
            exit 1
            ;;
    esac
done

build_rootfs

echo "Root filesystem built successfully at ~/tinospple_initrd.img"
