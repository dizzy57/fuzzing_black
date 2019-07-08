# fuzzing_black

A small set of scripts to showcase fuzzing `black` with `python-afl`  
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Slides

You can view slides online at https://talks.godoc.org/github.com/dizzy57/fuzzing_black/fuzzing_black.slide

## How to start fuzzing:

1. Split test cases into small chunks with `split_tests_into_corpus.py`.
2. Get python [grammar file](https://raw.githubusercontent.com/python/cpython/master/Grammar/Grammar).
2. Generate dictionary from the grammar with `extract_tokens_from_grammar.py > python.dict`.
3. Set up `PYTHONPATH` environment so that `import black` imports the development version of `black`.
4. Run `py-afl-fuzz -i afl_input/ -o afl_output/ -x python.dict -- python fuzz_persistent.py`.

## License

### The [Unlicense](http://unlicense.org):

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
