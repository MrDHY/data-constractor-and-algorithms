#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/6/30 12:01

import random

# <class 'list'>: [6, 20, 11, 4, 19, 12, 8, 10, 3, 17, 29, 26, 22, 14, 27, 25, 24, 13, 9, 15, 21, 28, 2, 16, 1, 23, 0, 18, 5, 7]

# 复杂度是O(nlog(n)), 稳定排序算法,并应用了分治法的算法思想
def merge_sort(seq):
    """注意这个递归调用顺序
    :param seq:
    :return:
    """
    if len(seq) <= 1:  # 递归出口
        return seq
    else:
        mid = int(len(seq)/2)
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])
    # print("left", left_half)
    # print("right", right_half)
    new_seq = merge_sorted_list(left_half, right_half)
    print("new seq", new_seq)
    return new_seq


def merge_sorted_list(sorted_a, sorted_b):
    """合并两个有序队列，返回一个新的有序队列
    :param sorted_a:
    :param sorted_b:
    :return:
    """
    length_a, length_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_seq = list()

    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1

    # 如果a 或者 b 中还有剩余元素，需要放到最后
    if a < length_a:
        new_sorted_seq.extend(sorted_a[a:])
    else:
        new_sorted_seq.extend(sorted_b[b:])

    return new_sorted_seq


def merge_sorted():
    seq = [6, 20, 11, 4, 19, 12, 8, 10, 3, 17, 29, 26, 22, 14, 27, 25, 24, 13, 9, 15, 21, 28, 2, 16, 1, 23, 0, 18, 5, 7]
    # random.shuffle(seq)
    seq = merge_sort(seq)
    assert seq == sorted(seq)


merge_sorted()