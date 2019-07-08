#!/usr/bin/env python

import re
from pathlib import Path

grammar = Path("Grammar").read_text()
inside_quotes = re.compile(r"'([^']+?)'")

token_set = {match.group(1) for match in inside_quotes.finditer(grammar)}
for token in sorted(token_set):
    print(f'"{token}"')
