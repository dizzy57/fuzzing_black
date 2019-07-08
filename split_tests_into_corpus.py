#!/usr/bin/env python

import itertools
import os
from pathlib import Path
from string import ascii_lowercase


def name_generator():
    for x in itertools.product("_" + ascii_lowercase, repeat=8):
        y = "".join(x).lstrip("_")
        if y:
            yield y


name = name_generator()
test_data = Path("black/tests/data")
out_dir = Path("afl_input/")

for file in test_data.glob("*.py"):
    lines = file.open().readlines()
    done = False
    while lines and not done:
        os.system("clear")
        print(file)
        print("===")
        for num, line in enumerate(lines[:30], start=1):
            print(f"{num:2}  {line}", end="")
        take = input("> ")
        if take == "":
            take = "1"
        if take != "0":
            take = int(take)
            if take < 0:
                del lines[:-take]
            else:
                took = lines[:take]
                out_file = out_dir / (next(name) + ".py")
                out_file.write_text("".join(took))
                del lines[:take]
        else:
            done = True
