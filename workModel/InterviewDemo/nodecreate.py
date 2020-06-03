# -*- coding:utf-8 -*-

'''
    author: anne
    content: 每个节点存储下一个节点的指针，每个节点由data和next组成
    step：1. 建立节点类； 2. 建立链表类
'''


# 节点类
class Node:

    # 构造一个节点
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

# 链表类
class SLinkedList:

    # 构造一个链表
    def __init__(self):
        self.head = None

    # 在链表开头插入节点
    def begin_insert(self, newdata):
        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
            return
        newnode.nextval = self.head  # 将新节点指向当前的头结点
        self.head = newnode  # 新节点变为头结点

    # 在链表末尾插入节点
    def end_insert(self, newdata):
        newnode = Node(newdata)
        if self.head is None:  # 若链表为空，则将新节点作为头结点
            self.head = newnode
            return
        laste = self.head  # 若链表不为空，对链表进行遍历
        while laste.nextval:
            laste = laste.nextval
        laste.nextval = newnode

    # 在链表中间插入节点
    def between_insert(self, between_data, newdata):
        if between_data is None:
            print("between_data isn't exit!")
            return
        newnode = Node(newdata)
        newnode.nextval = between_data.nextval
        between_data.nextval = newnode

    # 遍历链表并打印
    def list_print(self):
        printnode = self.head
        while printnode is not None:
            print(printnode.dataval)
            printnode = printnode.nextval
        return


list1 = SLinkedList()
list1.head = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wed')

list1.head.nextval = e2
e2.nextval = e3

list1.begin_insert('Sun')
list1.end_insert('Fri')
list1.between_insert(e2.nextval,'Thu')
list1.list_print()