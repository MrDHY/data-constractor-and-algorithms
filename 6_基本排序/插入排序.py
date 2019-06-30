#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/6/30 11:27

import random


# 复杂度: O(n^2), 两个循环
def insert_sort(seq):
    """
    :param seq:
    :return:
    """
    n = len(seq)
    for i in range(1, n):
        value = seq[i]    # 首先, 先取到这个这个位置的值，用于后续比较
        pos = i           # 拿到这个值的索引
        while pos > 0 and value < seq[pos - 1]:   # 把这个值和前面有序数组冒泡反序比较，如果小于我们要比较的值
            seq[pos] = seq[pos-1]                 # 则把两个值互换位置
            pos -= 1                              # 如果一直小于前面的值，则一直往前移位
        seq[pos] = value
    return seq


def test_insert_sort():

    seq = list(range(10))
    random.shuffle(seq)
    insert_sort(seq)
    assert seq == sorted(seq)