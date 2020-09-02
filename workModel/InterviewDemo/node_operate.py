# -*- coding:utf-8 -*-

'''
    author: anne
    content: 每个节点存储下一个节点的指针，每个节点由data和next组成
    step：1. 建立节点类； 2. 建立链表类
    结点(也可以叫节点或元素)，每一个结点有两个域，左边部份叫值域，用于存放用户数据；右边叫指针域，一般是存储着到下一个元素的指针
    head结点，head是一个特殊的结节，head结点永远指向第一个结点
    tail结点，tail结点也是一个特殊的结点，tail结点永远指向最后一个节点
    None，链表中最后一个结点指针域的指针指向None值，因也叫接地点，所以有些资料上用电气上的接地符号代表None
'''


# 节点类
class Node:

    # 构造一个节点
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None

# 链表类
class LinkedList:

    # 构造一个链表,初始化head和tail节点
    def __init__(self):
        self.head = None
        self.tail = None

    # 在链表开头插入节点
    def begin_insert(self, newdata):
        newnode = Node(newdata)
        if self.head is None:       # 判断是否是空链表
            print('list is none!!!')
            self.head = newnode
            return
        newnode.next = self.head  # 将新节点next指向当前的头结点
        self.head = newnode     # 头结点next指向新节点

    # 在链表末尾插入节点
    def end_insert(self, newdata):
        newnode = Node(newdata)
        if self.head is None:  # 若链表为空，则将head节点指向新节点
            self.head = newnode
            return
        tail = self.head  # 若链表不为空，对链表进行遍历，设定一个尾节点
        while tail.next:
            tail = tail.next
        tail.next = newnode

    # 在链表中间插入节点
    def mid_insert(self, between_data, newdata):
        if between_data is None:
            print("between_data isn't exit!")
            return
        newnode = Node(newdata)
        newnode.next = between_data.next
        between_data.next = newnode

    # 删除链表中某个节点
    def remove(self, idx):
        cur = self.head
        cur_idx = 0
        if self.head is None:  # 空链表时
            raise Exception('The list is an empty list!')
        while cur_idx < idx - 1:  # 遍历链表
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index!')
            cur_idx += 1
        if idx == 0:   # 当删除第一个节点
            self.head = cur.next
            cur = cur.next
            return
        if self.head is self.tail:  # 只有一个节点的链表
            self.head = None
            self.tail = None
            return
        cur.next = cur.next.next
        if cur.next is None:  # 删除的是最后一个节点时
            self.tail = cur

    #

    # 遍历链表并打印
    def list_print(self):
        printnode = self.head
        while printnode is not None:
            print(printnode.data)
            printnode = printnode.next
        return

if __name__ == '__main__':
    list1 = LinkedList()
    list1.head = Node('Mon')
    e2 = Node('Tue')
    e3 = Node('Wed')

    list1.head.next = e2
    e2.next = e3

    list1.begin_insert('Sun')
    list1.end_insert('Fri')
    list1.mid_insert(e2.next,'Thu')
    list1.remove(2)
    list1.list_print()