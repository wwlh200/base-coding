# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, x, val=None):
        self.val = x
        self.next = val

# 在单链表前插入节点


def addBefore(head, new):
    new.next = head
    head = new
    return head

# 在单链表中插入节点


def addMiddle(head, position, new):
    ln = head
    while head.next:
        if head.val == position:
            new.next = head.next
            head.next = new
            break
        head = head.next
    head = ln
    return head


# 在单链表后插入节点
def addAfter(head, new):
    ln = head
    # while head.next:
    #     head = head.next
    # head.next = new
    # new.next = None
    while head:
        if head.next == None:
            head.next = new
            new.next = None
            break
        head = head.next
    head = ln
    return head

# 生成链表


def generatorNodeList(m, n):
    i = m
    listNode1 = ListNode(-1)
    while i < n:
        addAfter(listNode1, ListNode(i))
        i += 1
    listNode1 = listNode1.next
    return listNode1


# # 初始化单链表
# listNode1 = generatorNodeList()

# print(listNode1)

# listNode2 = addBefore(listNode1, ListNode(0))

# print(listNode2)

# listNode3 = addMiddle(listNode2, 2, ListNode(2.5))

# print(listNode3)
