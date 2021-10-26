class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def loop(ln):
    d = set()
    while(ln):
        if ln in d:
            return True
        else:
            d.add(ln)
            ln = ln.next
    return False

