#!/usr/bin/env bash
cd /usr/src/googletest/googletest
mkdir build
cd build
cmake ..
make
cp libgtest* /usr/lib/
cd ..
rm -rf build

mkdir /usr/local/lib/googletest
ln -s /usr/lib/libgtest.a /usr/local/lib/googletest/libgtest.a
ln -s /usr/lib/libgtest_main.a /usr/local/lib/googletest/libgtest_main.a