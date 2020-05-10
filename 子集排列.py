#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/10 19:09


def get_son_set(List):
    global result
    if len(List) <= 2:
        return
    for i in range(len(List)):
        first = List[i]
        last = List[:i] + List[i + 1:]
        print(first, last)
        if [first] not in result:
            result.append([first])
        if last not in result:
            result.append(last)
        get_son_set(List=last)


if __name__ == '__main__':
    result = []
    get_son_set(List=[1, 2, 3, 4])
    print(result)
