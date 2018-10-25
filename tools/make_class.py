# -*- coding: utf-8 -*-
"""
generate default src/ test package using template

glob, gtest, boost library
"""

if __name__ == '__main__':
    import os
    import argparse

    parser = argparse.ArgumentParser(description='calss generators')
    parser.add_argument('class_type', type=str, help='make executable file')
    parser.add_argument('name', type=str, help='make unittest file')

    args = parser.parse_args()

    if args.method == 'src':
        root_path = '../src/'
        target_path = os.path.join(root_path, args.name)
        target_file = os.path.join(target_path, 'main.cpp')
        if not os.path.exists(target_path):
            with open(target_file, 'w') as fp:
                pass
