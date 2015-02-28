#!/usr/bin/env python
# encoding: utf-8
"""
    一些简单的文本处理函数
"""
import sys
import re

def unify_blank(line):
    """
        将line中所有空格（包括行中的\t换行等）都换为separator
    """
    pattern = re.compile(r'(\s+)')
    print pattern.sub(func, line)

def func(match):
    return ' '

def main():
    """
        执行函数
    """
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        unify_blank(line)

if __name__ == '__main__':
    main()
