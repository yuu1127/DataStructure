#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:01:54 2018

@author: yuta
"""

from stack import *

from queue import *


tree = {'A':['B','C','D'],
        'C':['E','F'],
        'F':['G'],
        'G':['H','L'],
        'D':['M'],
        'M':['N','O']
        }

def explore_depth_first():
    stack = Stack()
    stack.push('A')
    while not stack.is_empty():
        node = stack.pop()
        print(node)
        if node in tree:
            for child in reversed(tree[node]):
                stack.push(child)

explore_depth_first()

def explore_depth_stack():
    stack = Stack()
    stack.push(['A'])
    while not stack.is_empty():
        path = stack.pop()
        print(path)
        if path[-1] in tree:
            for child in reversed(tree[path[-1]]):
                stack.push(path + [child])

explore_depth_stack()


def explore_depth_first1():
    queue = Queue()
    queue.enqueue('A')
    while not queue.is_empty():
        node = queue.dequeue()
        print(node)
        if node in tree:
            for child in tree[node]:
                queue.enqueue(child)

explore_depth_first1()


def explore_depth_queue():
    queue = Queue()
    queue.enqueue(['A'])
    while not queue.is_empty():
        path = queue.dequeue()
        print(path)
        if path[-1] in tree:
            for child in tree[path[-1]]:
                queue.enqueue(path + [child])

explore_depth_queue()
    