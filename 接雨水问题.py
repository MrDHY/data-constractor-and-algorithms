#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/10 19:25

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        res = 0
        left_max = 0
        right_max = len(height) - 1

        while left < right:
            if height[left] > height[right]:
                if height[right_max] < height[right]:
                    right_max = right
                    right = right - 1
                else:
                    res += height[right_max] - height[right]
                    right = right - 1

            if height[left] <= height[right]:
                if height[left_max] < height[left]:
                    left_max = left
                    left = left + 1
                else:
                    res += height[left_max] - height[left]
                    left = left + 1
        return res