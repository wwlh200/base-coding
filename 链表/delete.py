import copy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 在单链表后插入节点


def addAfter(head, new):
    ln = head
    while head.next:
        head = head.next
    head.next = new
    head = ln
    new.next = None
    return head


# 初始化单链表
i = 1
listNode1 = ListNode(-1)
while i < 5:
    addAfter(listNode1, ListNode(i))
    i += 1
listNode1 = listNode1.next

print(listNode1)

# 删除单链表第一个节点


def deleteFirst(head):
    if head:
        head = head.next
    return head

# 删除单链表中间节点


def deleteMiddle(head, position):
    ln = head
    while ln:
        if ln.next.val == position:
            ln.next = ln.next.next
            break
        ln = ln.next
    return head
# 删除单链表最后一个节点


def deleteLast(head):
    ln = head
    while ln.next.next:
        ln = ln.next
    ln.next = ln.next.next
    return head


listNode2 = deleteFirst(copy.deepcopy(listNode1))
print(listNode2)


listNode3 = deleteMiddle(copy.deepcopy(listNode1), 2)
print(listNode3)

listNode4 = deleteLast(copy.deepcopy(listNode1))
print(listNode4)
