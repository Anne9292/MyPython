class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def AtBegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

    def RemoveNode(self, Removekey):
        HeadVal = self.head
        # if (HeadVal is not None):
        #     if (HeadVal.data == Removekey):
        #         self.head = HeadVal.next
        #         HeadVal = None
        #         return
        while HeadVal is not None:
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if HeadVal is None:
            return
        prev.next = HeadVal.next

    def LListprint(self):
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.AtBegining("Mon")
    llist.AtBegining("Tue")
    llist.AtBegining("Wed")
    llist.AtBegining("Thu")
    llist.RemoveNode("Tue")
    llist.LListprint()