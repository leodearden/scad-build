#!/usr/bin/python
import sys, os
print sys.path
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/fabricate')
print sys.path
from fabricate import *

sources = ['gear-mother-mold-base', 'gear-mother-mold-lid', 'gear-mother-mold-wall', 'gear-mother-mold-sub-base-back', 'gear-mother-mold-sub-base-left', 'gear-mother-mold-sub-base-right', 'gear-mother-mold-sub-runners']

def build():
    for source in sources:
        run('openscad', source + '.scad', '-o', source + '.stl')

def clean():
    autoclean()

main(parallel_ok=True, jobs=8)
