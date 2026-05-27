set -e

echo "Starting Kernel configuration process"

cd linux-7.1-rc5

echo "Configuring the kernel with default settings"

make defconfig

echo "Kernel configured successfully with default settings"
