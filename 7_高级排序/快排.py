#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/6/30 18:37


# [6, 3, 4, 1, 5, 7, 2, 6, 8, 0]
def quick_sort(array):
    size = len(array)
    if not array or size < 2:
        return array

    pivot_index = 0
    pivot = array[pivot_index]
    less_part = [array[i] for i in range(size) if array[i] <= pivot and pivot_index != i]
    great_part = [array[i] for i in range(size) if array[i] > pivot and pivot_index != i]
    return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def _quick():
    # import random
    # seq = list(range(10))
    # random.shuffle(seq)
    seq = [6, 3, 4, 1, 5, 7, 2, 6, 8, 0]
    assert quick_sort(seq) == sorted(seq)

_quick()

### 为什么 快排不稳定?
'''
你想想 从左到右比较的时候 你的array可以分成这样四部分p  |  lower |  higher | unvisitedp指的是pivotal，
lower指小于p的部分，unvisited指还未访问到，| 是分割线。例如：5  |  3 1 2  |  9 7 8 9 | 4 6 3这时遍历unvisited部分 
 刚到了4 (array[8])  显然4<5 ，这是4应该从 unvisited 部分去到 lower 部分。 
 因此 higher部分第一个元素 9 (array[4]) 和 4互换。变成了这样：5  |  3 1 2 4 | 7 8 9 9 |  6 3注意！
 这时这个9 (array[4]) 被换到了 后面那个9 (array[7])的 后面。这就不稳定了。

'''
