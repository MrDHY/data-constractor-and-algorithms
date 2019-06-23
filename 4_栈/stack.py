#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/6/23 12:03

from collections import deque


# 第一种写法
class MyDeque(object):

    def __init__(self):
        self._item_node = deque()

    def pop(self):
        return self._item_node.pop()

    def push(self, value):
        return self._item_node.append(value)



# 第二种写法
class Node(object):
    __slots__ = ("value", "prev", "next")

    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircularDoubleLinkedList(object):
    """ 循环双端链表 ADT
    多了个循环就是把 root的prev 指向tail节点
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.length = 0
        node = Node()
        self.root = node
        self.root.next, self.root.prev = node, node

    def head(self):
        """ 返回头节点

        :return:
        """
        return self.root.next

    def tail(self):
        """ 获取尾部节点

        :return:
        """
        return self.root.prev

    def __len__(self):
        return self.length

    def iter_item(self):
        """ 循环节点

        :return:
        """
        if self.root.next is self.root:  # 这里我没加判断
            return
        curnode = self.root.next
        while curnode.next is not self.root:  # 这里我判断出错了
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        """ 转为迭代器时调用

        :return:
        """
        for item in self.iter_item():
            yield item.value

    def append(self, value):
        """ 添加元素

        :param value:
        :return:
        """
        if self.maxsize and self.length >= self.maxsize:
            raise Exception("LinkedList is Full")

        node = Node(value=value)
        tailnode = self.tail()
        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        """ 从头部增加节点
        增加都得先判断长度，然后正常增加即可
        :param value:
        :return:
        """
        if self.maxsize and self.length >= self.maxsize:
            raise Exception("LinkedList is Full")

        node = Node(value)
        headnode = self.head()
        self.root.next = node
        node.prev = self.root
        node.next = headnode
        self.length += 1

    def remove(self, node):
        """ 移除节点
        思路: 如果这个节点是root， return
        然后正常移除节点节点即可，self.length - 1
        :param node:
        :return:
        """
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def find(self, value):
        """ 查找元素
        思路: 还是一样，如果这个链表为空，直接返回
        然后遍历所有节点，当查到这个节点的value是这个值的时候,return 出去即可
        :param value:
        :return:
        """
        if self.root.next is self.root:
            return
        index = 0
        for node in self.iter_item():
            if node.value == value:
                return index
            else:
                index += 1
        return -1

    def popleft(self):
        """ pop元素
        先得判断这个双链表是否为空: self.root.next is self.root
        然后再正常pophead即可
        :return:
        """
        if self.root.next is self.root:
            return

        head_node = self.head()
        self.root.next = head_node.next
        head_node.next.prev = self.root
        self.length -= 1
        del head_node

    def reverse(self):
        """ 反转双链表
         第一次这里我全写错了，思路从root.prev--->curnode.next=self.root结束，
         yield节点，然后再返回最后最后一次的节点
        :return:
        """
        if self.root.next is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode


class Deque(CircularDoubleLinkedList):

    def pop(self):
        if len(self) == 0:
            raise Exception("empty node")

        tailnode = self.tail()
        value = tailnode.value
        self.remove(tailnode)
        return value


def test_deque():

    d = Deque()
    d.append(1)
    assert len(d) == 1

    m = d.pop()
    assert m == 1
    assert len(d) == 0

test_deque()