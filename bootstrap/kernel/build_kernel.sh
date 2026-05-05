set -e
echo "Starting kernel build process"

export LINUX_SOURCE_DIR=$(pwd)/../linux-7.1-rc2

if [ ! -d "$LINUX_SOURCE_DIR" ]; then
    echo "Kernel source directory not found. Please run fetch_kernel.sh first or check the directory path."
    exit 1
fi
echo "Kernel source directory found at: $LINUX_SOURCE_DIR"

cd $LINUX_SOURCE_DIR

echo "Starting make to build the kernel"
make -j$(nproc)
echo "Kernel build process completed successfully"