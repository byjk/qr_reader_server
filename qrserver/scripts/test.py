#!/usr/bin/python
import sys

m = 'hello world from test.py script'
if len(sys.argv) > 1:
    m = sys.argv[1]
print (m)
