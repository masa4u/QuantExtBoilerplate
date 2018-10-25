#!/usr/bin/env bash
cd /tmp
git clone https://github.com/google/glog
cd glog
cmake . -DWITH_GFLAGS=OFF
make
make install
cd ..
rm -rf glog
