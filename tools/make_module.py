# -*- coding: utf-8 -*-
"""
generate default src/ test package using template

glob, gtest, boost library
"""


src_template = open('./template/src.cpp', 'r').read()
test_template = open('./template/test.cpp', 'r').read()

if __name__ == '__main__':
    import os
    import argparse

    parser = argparse.ArgumentParser(description='module generators')
    parser.add_argument('method', type=str, help='make executable file')
    parser.add_argument('name', type=str, help='make unittest file')

    args = parser.parse_args()

    if args.method == 'src':
        root_path = '../src/'
        target_path = os.path.join(root_path, args.name)
        target_file = os.path.join(target_path, 'main.cpp')
        if not os.path.exists(target_path):
            os.mkdir(target_path)
            with open(target_file, 'w') as fp:
                fp.write(src_template)

    print(args.method)
    print(args.name)
