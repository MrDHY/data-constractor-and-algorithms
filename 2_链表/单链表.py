# /usr/bin/env python
# -*- coding:utf-8 -*-


class Node(object):

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkList(object):

    def __init__(self, maxsize=None):
        self.root = Node()
        self.maxsize = maxsize
        self.length = 0
        self.tail = None

    def __len__(self):
        return self.length

    def append(self, value):
        """
        思路: 1，append都得先判断链表长度
             2. 因为append依赖于tail.所以我们在这儿要对tail进行判断，为none的时候添加
             3. tail不为None的时候添加
        :param value:
        :return:
        """
        if self.maxsize and self.length >= self.maxsize:
            raise Exception("full LinkList")

        node = Node(value)
        if self.tail is None:
            self.tail = node
            self.root.next = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def apendleft(self, value):
        """
        思路参考于append，也要对tail是否存在进行判断
        :param value:
        :return:
        """
        if self.maxsize and self.length >= self.maxsize:
            raise Exception("full LinkList")

        node = Node(value)

        if self.tail is None:
            self.tail = node

        head_node = self.root.next
        self.root.next = node
        node.next = head_node
        self.length += 1

    def popleft(self):
        """
        思路: 如果headnode和tailnode一样的话,那说明只有一个节点
        但是要更新self.tail
        :return:
        """
        if self.length <= 0:
            raise Exception("Empty LinkList")

        headnode = self.root.next
        if headnode is self.tail:
            self.tail = None
        nextnode = headnode.next
        self.root.next = nextnode
        self.length -= 1
        del headnode
        return

    def __iter__(self):
        """实现list方法"""
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        """
        思路: 从self.head节点开始遍历，当遍历到curnode.next is self.tail时，退出
        然后返回最后节点
        :return:
        """
        curnode = self.root.next
        while curnode is not self.tail:
                yield curnode
                curnode = curnode.next
        if curnode is not None:
            yield curnode

    def clear(self):
        """
        思路，遍历所有节点，删除，更新head,tail.length
        :return:
        """
        for node in self.iter_node():
            del node

        self.root.next = None
        self.length = 0
        self.tail = None

    def find(self, value):

        i = 0
        for node in self.iter_node():
            if node.value == value:
                return i
            else:
                i += 1
        return -1

    def remove(self, value):
        """
        思路: 遍历所有节点，找到node.value=value时，删除节点
        需要注意当前节点是否为tail节点，如果为tail节点时，需要更新tail节点为当前节点的前一个节点
        :param value:
        :return:
        """
        prenode = self.root
        for node in self.iter_node():
            if node.value == value:
                if node is self.tail:
                    self.tail = prenode
                prenode.next = node.next
                self.length -= 1
                del node
                return 1
            else:
                prenode = node
        return -1

    def reverse(self):
        """
        思路: curnode=self.root.next， 把当前节点的next指向之前节点的prev
        遍历的第一个节点的是headnode，所以这个节点的next=None,
        需要用一个prenode来记录上一个节点
        :return:
        """
        curnode = self.root.next
        prenode = None
        self.tail = curnode
        while curnode:
            nextnode = curnode.next
            curnode.next = prenode
            if nextnode is None:
                self.root.next = curnode
            prenode = curnode
            curnode = nextnode


def test_linklist():
    l1 = LinkList()
    l1.append(1)
    assert len(l1) == 1
    l1.append(2)
    assert len(l1) == 2
    l1.append(3)
    l1.append(4)

    l1.popleft()
    l1.popleft()
    assert (list(l1)) == [3, 4]

    a = l1.find(3)
    assert a == 0

    l1.remove(4)
    assert list(l1) == [3]

    l1.append(2)
    l1.reverse()
    print(list(l1))


test_linklist()