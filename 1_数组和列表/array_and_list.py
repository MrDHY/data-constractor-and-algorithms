#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/6/16 11:48


from array import array

arr = array("u", "sssc")

print(arr[-1])


class Array(object):

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size
        self.start = 0

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self,  value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < len(self._items):
            val = self._items[self.start]
            self.start += 1
            return val
        else:
            raise StopIteration


def test_array():
    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1
    assert len(a) == 10

    for i in iter(a):
        print(i)
