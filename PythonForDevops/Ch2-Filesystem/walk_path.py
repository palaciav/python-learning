#! /usr/bin/python3

import os, fire

def walk_path(parent_path):
    for parent_path, directories, files in os.walk(parent_path):
        print(f"Checking: {parent_path}")
        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            last_access = os.path.join(parent_path, file_name)
            size = os.path.getsize(file_path)
            print(f"File: {file_path}")
            print(f"\tLast accessed: {last_access}")
            print(f"\tSize: {size}")

if __name__ == '__main__':
    fire.Fire()