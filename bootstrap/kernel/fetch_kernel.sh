set -e

echo "Fetching and extracting the kernel source"

wget https://git.kernel.org/torvalds/t/linux-7.1-rc2.tar.gz

tar -xf linux-7.1-rc2.tar.gz

echo "Kernel source fetched and extracted successfully"