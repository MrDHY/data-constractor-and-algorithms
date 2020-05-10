#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/10 17:40


class Solution:
    def longestPalindrome(self, s: str) -> str:
        firststr = ''
        secondstr = ''
        for each in range(len(s) if len(s) < 1000 else 1000):
            m, n = each, each
            while m >= 0 and n <= len(s) - 1 and s[m] == s[n]:
                    if len(firststr) <= n - m + 1: firststr = s[m:n + 1]
                    m -= 1
                    n += 1
            m, n = each, each + 1
            while m >= 0 and n <= len(s) - 1 and s[m] == s[n]:
                    if len(secondstr) <= n - m + 1: secondstr = s[m:n + 1]
                    m -= 1
                    n += 1
        return firststr if len(firststr) > len(secondstr) else secondstr


s = Solution()
print(s.longestPalindrome("abccbacacyy"))