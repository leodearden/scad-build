#!/usr/bin/python
import sys, os, glob
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/fabricate')
from fabricate import *

sources = glob.glob('*-stl.scad')

def build():
    for source in sources:
        run('openscad', source, '-o', source[:-9] + '.stl')

def clean():
    autoclean()

main(parallel_ok=True, jobs=8)
