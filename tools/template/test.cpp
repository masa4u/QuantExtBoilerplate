#include <stdio.h>

#include <gtest/gtest.h>

#if defined(WIN32) && defined(_DEBUG)
#include <vld.h>
#endif  // defined(_WIN32) && defined(_DEBUG)

GTEST_API_ int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}