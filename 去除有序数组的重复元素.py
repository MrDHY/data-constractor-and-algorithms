#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/10 19:01


def removeDuplicated(s):
    n = len(s)
    if n == 0: return 0

    slow = 0
    fast = 1

    while fast < n:
        if s[fast] != s[slow]:
            slow += 1
            s[slow] = s[fast]
        fast += 1
    return slow + 1

s = [1, 1, 3, 4, 4]
print(removeDuplicated(s))
slow_idx = removeDuplicated(s)
print(s[:slow_idx])