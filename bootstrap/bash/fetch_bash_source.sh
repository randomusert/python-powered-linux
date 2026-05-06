#!/bin/bash
set -e

echo "Fetching bash source archive from ftp.gnu.org"

wget https://ftp.gnu.org/gnu/bash/bash-5.3.tar.gz

echo "Extracting bash source archive"

tar -xf bash-5.3.tar.gz

echo "Bash source fetched and extracted successfully"