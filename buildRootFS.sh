set -e
set -o pipefail


check_path_to_root() {
    if [ ! -d "$TINOSPPLE_ROOTFS" ]; then
        echo -e "Error: TINOSPPLE_ROOTFS directory does not exist or the variable is not set as a argument. Please do buildRootFS.sh $TINOSPPLE_ROOTFS=/path/to/tinospple_rootfs"
        exit 1
    fi
}

find $TINOSPPLE_ROOTFS -print0 | cpio --null -ov --format=newc | gzip -9 > "$HOME/tinospple_initrd.img"

echo "Root filesystem built successfully at $HOME/tinospple_initrd.img"