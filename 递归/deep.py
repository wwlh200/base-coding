# fib
# 阶乘
# 链表反转
# 求和1+2+3+4+....+100


# 干什么 前后相加
# 停止条件 n==1或者n==2
# 重复条件 当前加前一个
def fib(n):
    if n == 1 or n == 2:
        return n
    sum = fib(n - 1) + fib(n - 2)
    return sum


print(fib(5))

# 干什么 前后相加
# 停止条件 n==1或者n==2
# 重复条件 当前加前一个


def avg(n):
    if n == 1 or n == 2:
        return n
    sum = n * avg(n-1)
    return sum


print(avg(5))


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class myListNode:
    def __init__(self):
        self.head = ListNode(0)
        self.size = 1

    def add_index(self, index, val):
        if index < 0 or index > self.size:
            return
        self.size = self.size+1
        ln = self.head
        for i in range(index-1):
            ln = ln.next

        new = ListNode(val)
        new.next = ln.next
        ln.next = new

    def get(self):
        return self.head

      # 干什么 反转过来
  # 停止条件 head=null,head.next=null
 # 重复条件 head.next=xx.next
    def reverse(self, head):
        if not head or not head.next:
            return head
        ret = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return ret


my = myListNode()
my.add_index(0, 3)
my.add_index(0, 2)
my.add_index(0, 1)

new = my.reverse(my.get())
print(new)
print(111)


# 求和1+2+3+4+....+100
# 干什么 累加
# 停止条件 i=1
# 重复条件 一直循环

def sum100(n):
    if n == 0 or n == 1:
        return n
    sum = n+sum100(n-1)
    return sum

print(sum100(5))