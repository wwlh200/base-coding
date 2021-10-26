// fib
// 阶乘
// 链表反转
// 求和1+2+3+4+....+100

// 干什么 前后相加
// 停止条件 n==1或者n==2
// 重复条件 当前加前一个
const fib = (n) => {
  if (n === 1 || n === 2) {
    return n;
  }
  sum = fib(n - 1) + fib(n - 2);
  return sum;
};

console.log(fib(5));

// 干什么 当前数*上一个数
// 停止条件 n==1或者n==2
// 重复条件 当前加前一个
const avg = (n) => {
  if (n === 1) {
    return n;
  }
  sum = n * avg(n - 1);
  return sum;
};

console.log(avg(5));

class ListNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

class myListNode {
  constructor() {
    this.head = new ListNode(0);
    this.size = 1;
    this.ret = null;
  }

  get() {
    return this.head;
  }

  insertIndex(val, index) {
    if (index < 0 || index > this.size) {
      return;
    }

    this.size++;
    let ln = this.head;
    for (let i = 0; i < index - 1; i++) {
      ln = ln.next;
    }
    let node = new ListNode(val);
    node.next = ln.next;
    ln.next = node;
  }
  // 干什么 反转过来
  // 停止条件 head=null,head.next=null
  // 重复条件 head.next=xx.next
  reserve(head) {
    if (!head || !head.next) {
      return head;
    }

    const ret = this.reserve(head.next);
    head.next.next = head;
    head.next = null;
    return ret;
  }
}

let my = new myListNode();

my.insertIndex(3, 0);
my.insertIndex(2, 0);
my.insertIndex(1, 0);
my.reserve(my.get());
console.log(my.get());

// 求和1+2+3+4+....+100
// 干什么 累加
// 停止条件 i=1
// 重复条件 一直循环

const sum100 = (n) => {
  if (n === 0 || n === 1) {
    return n;
  }
  let sum = n + sum100(n - 1);
  return sum;
};

console.log(sum100(5));
