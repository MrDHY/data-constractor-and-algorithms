#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/6/30 10:51

import random


# 复杂度 O(n^2),两个循环
def bubble_sort(seq):
    """
    思路分析: 从第一个元素开始，两两对比，直到倒数第二个，然后从第二个开始，两两对比...
    需要注意的是，最后一个数不用再比较了，所以n-1
    :param seq:
    :return:
    """
    n = len(seq)
    for i in range(n-1):
        # print(seq)
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq


def test_bubble_sort():
    seq = list(range(50))
    random.shuffle(seq)
    bubble_sort(seq)
    assert seq == sorted(seq)

