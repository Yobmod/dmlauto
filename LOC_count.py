#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Created on Wed Dec 13 15:24:53 2017
@author: yobmod"""

import os

def countlines(start, lines=0, header=True, begin_start=None):
    if header:
        print('{:>10} |{:>10} | {:<20}'.format('ADDED', 'TOTAL', 'FILE')) # print column titles
        print('{:->11}|{:->11}|{:->20}'.format('', '', '')) # print line
    ext_tup = ('.py', '.pyx', '.c', '.cpp', '.js', '.jsx', '.ts', '.tsx')
    for thing in os.listdir(start):
        thing = os.path.join(start, thing)
        if os.path.isfile(thing):

            if thing.endswith(ext_tup):
                with open(thing, 'r') as f:
                    newlines = f.readlines()
                    newlines = len(newlines)
                    lines += newlines
                    
                    if begin_start is not None:
                        reldir_of_thing = '.' + thing.replace(begin_start, '')
                    else:
                        reldir_of_thing = '.' + thing.replace(start, '')

                    print('{:>10} |{:>10} | {:<20}'.format(
                            newlines, lines, reldir_of_thing))
                    
    for thing in os.listdir(start):
        thing = os.path.join(start, thing)
        if os.path.isdir(thing):
            if "vendor" in thing:
                pass
            else:
                lines = countlines(thing, lines, header=False, begin_start=start)
    return lines

def pyLines(directory: str) -> int:
    exc_list = ["vendor", "dist", "build", "energenie"]
    py_lines = 0
    for thing in os.listdir(directory):
        thing = os.path.join(directory, thing)
        if os.path.isfile(thing):
            with open(thing, 'r') as f:
                if thing.endswith('.py') or thing.endswith('.pyx'):
                    newlines = f.readlines()
                    py_lines = py_lines + len(newlines)
        elif os.path.isdir(thing):
            if any(x in thing for x in exc_list):
                pass
            else:
                lines = pyLines(thing)
                py_lines = py_lines + lines
    return py_lines

#textList = ['a.tif','b.jpg','c.doc','d.txt','e.tif'];
#filteredList = filter(lambda x:x.endswith('.tif'), textList)
    #or
#filtered = regexp( filelist ,'(\w*.txt$)|(\w*.doc$)','match')
#filtered = [filtered{:}]

def jsLines(directory):
    js_lines = 0
    ts_lines = 0
    for thing in os.listdir(directory):
        thing = os.path.join(directory, thing)
        if os.path.isfile(thing):
            with open(thing, 'r') as f:
                if thing.endswith('.js') or thing.endswith('.jsx'):
                    newlines = f.readlines()
                    js_lines = js_lines + len(newlines)
                elif thing.endswith('.ts') or thing.endswith('.tsx'):
                    newlines = f.readlines()
                    ts_lines = ts_lines + len(newlines)
    jsts_lines = js_lines + ts_lines
    if ts_lines == 0:
        return js_lines
    else:
        jsts_lines = str(jsts_lines) + "(" + str(ts_lines) + ")"
        return jsts_lines

def cLines(directory):
    c_lines = 0
    for thing in os.listdir(directory):
        thing = os.path.join(directory, thing)
        if os.path.isfile(thing):
            with open(thing, 'r') as f:
                if thing.endswith('.c') or thing.endswith('.cpp'):
                    newlines = f.readlines()
                    c_lines = c_lines + len(newlines)
        elif os.path.isdir(thing):
            if "vendor" in thing:
                pass
            else:
                lines = cLines(thing)
                c_lines = c_lines + lines
    return c_lines
        

dir = os.getcwd()
countlines(dir)
j = pyLines(dir)
k = jsLines(dir)
l = cLines(dir)

print(j, k, l)
'''
import os
from os.path import isfile, join


def countLinesInPath(path,directory):
    count=0
    for line in open(join(directory,path), encoding="utf8"):
        count+=1
    return count

def countLines(paths,directory):
    count=0
    for path in paths:
        count=count+countLinesInPath(path,directory)
    return count

def getPaths(directory):
    return [f for f in os.listdir(directory) if isfile(join(directory, f))]

def countIn(directory):
    return countLines(getPaths(directory),directory)

dir = os.getcwd()
LOC = countIn(dir)

print(dir)
print(LOC)
'''