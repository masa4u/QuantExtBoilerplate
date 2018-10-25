FROM ubuntu:bionic

RUN apt-get update && apt-get install -gy cmake build-essential \
    lcov \
    python-pip wget \
    libgoogle-glog-dev libgtest-dev \
    libboost-dev

RUN rm -rf /var/lib/apt/lists/*

# build google test
ADD ./build_googletest.sh /root/build_googletest.sh
RUN /root/build_googletest.sh

# build glog
ADD ./build_glog.sh /root/build_glog.sh
RUN /root/build_glog.sh

ONBUILD user root
ONBUILD WORKDIR /