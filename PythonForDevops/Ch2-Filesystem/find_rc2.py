#! /usr/bin/python3

import os, fire

def find_rc(rc_name==".examplerc"):

    # Check for Env variable
    var_name = "EXAMPLERC_DIR"
    example_dir = os.environ.get(var_name)