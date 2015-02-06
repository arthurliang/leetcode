'''
Created on Dec 24, 2014

@author: Arthur
'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SinglyLinkedList:
    def __init__(self, head = None):
        self.listhead = head

    def DeserializationOnOJ(self, srlztnOnOJ):
        if srlztnOnOJ == "{}":
            return True

        datalist = srlztnOnOJ[1:-1].split(',')

        self.listhead = ListNode(None)
        currentPointer = self.listhead

        for index in range(len(datalist)):
            currentPointer.val = int(datalist[index])
            if index != len(datalist) - 1:
                currentPointer.next = ListNode(None)
                currentPointer = currentPointer.next

        return True


    def SerializationOnOJ(self):
        srlztnOnOJ = "{"

        currentPointer = self.listhead

        while currentPointer is not None:
            srlztnOnOJ += str(currentPointer.val)
            currentPointer = currentPointer.next
            if currentPointer is not None:
                srlztnOnOJ += ','

        return srlztnOnOJ + '}'
