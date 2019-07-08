#!/usr/bin/env python
import os
import sys

import afl
from black import FileMode, format_file_contents

mode = FileMode(
    target_versions=set(), line_length=88, is_pyi=False, string_normalization=True
)


stdin = sys.stdin.buffer
while afl.loop(10000):
    try:
        stdin.seek(0)
        format_file_contents(stdin.read().decode("ascii"), fast=False, mode=mode)
    except AssertionError as e:
        if "AST error message" in e.args[0]:
            pass
        else:
            os._exit(1)
    except:
        pass
os._exit(0)
