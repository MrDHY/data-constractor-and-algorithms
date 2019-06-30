#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/6/30 11:18

import random


# 复杂度: O(n^2)，两个循环
def select_sort(seq):
    """
    思路分析: 从第一个开始，比较它后面的元素，有没有比他小的，如果比它，则调换位置
    :param seq:
    :return:
    """
    n = len(seq)
    for i in range(n-1):
        for j in range(i+1, n):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
    print("last", seq)
    return seq


def test_select_sort():
    seq = list(range(10))
    random.shuffle(seq)
    print("first", seq)
    select_sort(seq)
    assert seq == sorted(seq)


test_select_sort()