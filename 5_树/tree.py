#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/6/23 12:39


node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]


class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


class Bintree(object):

    def __init__(self, root):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        """通过节点信息构造二叉树
        第一次遍历我们构造的node节点
        第二次遍历我们给root和孩子赋值
        最后我们用root初始化这个类并返回一个对象
        :param node_list:
        :return:
        """
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)

        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)

    def preorder_trav(self, subtree):
        """ 根序遍历  中-->左-->右
            中序遍历  左-->中-->右
            后序遍历  左-->右--中
        :param subtree:
        :return:
        """
        if subtree is not None:

            self.preorder_trav(subtree.left)

            self.preorder_trav(subtree.right)
            print(subtree.data)

    def layer_trav(self, subtree):
        """ 层序遍历

        :param subtree:
        :return:
        """
        cur_nodes = [subtree]  # current layer nodes
        next_nodes = []
        while cur_nodes or next_nodes:
            for node in cur_nodes:
                print(node.data)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            cur_nodes = next_nodes  # 继续遍历下一层
            next_nodes = []

    def reverse(self, subtree):
        """ 反转二叉树

        :param subtree:
        :return:
        """
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)


btree = Bintree.build_from(node_list)
print(btree.preorder_trav(btree.root))