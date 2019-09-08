#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ File singleLinkedList.py
# @ Description 链表操作
# @ Author alexchung
# @ Time 8/9/2019 AM 11:27

"""
chainTable operation
"""


class Node(object):
    """
    chain node
    """
    def __init__(self, val, next=None, prev=None):
        """
        :param x: val
        """
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        """
        输出 node 数据
        :return:
        """
        return str(self.val)


class singleLinkedList(object):
    """
    single link list
    """
    def __init__(self, maxsize=None):
        """
        初始化链表
        :param maxsize: 链表容量
        """
        self.maxsize = maxsize
        self.head = None  # 链表头游标(cursor)
        self.tail = None  # 链表尾游标(cursor)
        self.length = 0

    def __len__(self):
        """
        链表长度
        :return:
        """
        return self.length

    def isEmpty(self):
        """
        链表是否为空
        :return:
        """
        return self.length == 0

    def append(self, val):
        """
        尾部添加数据
        :param data:
        :return:
        """
        if self.length == self.maxsize:
            raise Exception('chain table is full')
        node = Node(val)
        # 判断链表是否为空
        if self.head is None:
            self.head = node

        # 否则链表不为空
        else:
            # 更新当前尾节点 指向新节点
            self.tail.next = node

        self.length += 1
        # 更新尾节点为新节点
        self.tail = node

    def insert(self, index, val):
        if self.length == self.maxsize:
            raise Exception('chain table is full')
        if index < 0 or index > self.length:
            raise Exception('out of range')

        node = Node(val)
        # 如果插入链表头
        if index == 0:
            node.next = self.head
            self.head = node

        # 插入链表其他位置
        else:
            current = self.head
            for i in range(1, index):
                current = current.next
            node.next = current.next
            current.next = node
        self.length += 1


    def traverseNode(self):
        """
        便利节点
        :return:
        """
        current = self.head
        while current:
            yield current
            current = current.next


if __name__ == "__main__":
    a = Node(2)
    l1 = singleLinkedList(10)

    l1.append(2)
    l1.append(3)
    l1.insert(0, 4)
    l1.insert(1, 5)
    for i in l1.traverseNode():
        print(i)
