echo "Starting kernel build process"
set LINUX_SOURCE_DIR=$(pwd)/../linux-7.1-rc2
if [! -d "$LINUX_SOURCE_DIR"]; then
    echo "Kernel source directory not found. Please run fetch_kernel.sh first or check the directory path."
    exit 1
fi