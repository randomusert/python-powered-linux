#!/bin/bash
set -e

echo "Building bash source"

export MAKEFILE_PATH=$(pwd)/Makefile

if [ ! -f "$MAKEFILE_PATH" ]; then
    echo "Makefile not found at: $MAKEFILE_PATH. Please Make sure you have configured bash source correctly before running this script."
    exit 1
fi

make -j$(nproc)


echo "Bash built successfully"