import copy

# 定义链表结构
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 根据数列生成链表
a = [1, 2, 3, 4]


def generatorListNode(arr):
    head = ListNode(arr[0])
    cur = head
    for i in arr[1:]:
        head.next = ListNode(i)
        head = head.next
    return cur


listNode1 = generatorListNode(a)


def reverse(ln):
    prev = None
    cur = ln
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev


listNode2 = reverse(copy.deepcopy(listNode1))

print(listNode2)
