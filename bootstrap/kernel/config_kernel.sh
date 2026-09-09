set -e

echo "Starting Kernel configuration process"

cd linux-7.3-rc2

echo "Configuring the kernel with default settings"

make defconfig

echo "Kernel configured successfully with default settings"
