// // ⽬目标数组
// var arr = [
//   { id: 3, parent: 2 },
//   { id: 1, parent: null },
//   { id: 2, parent: 1 },
// ];

// const sortArr = arr.sort((a, b) => b.parent - a.parent);
// console.log(sortArr);
// const result = sortArr.reduce((total, current) => {
//   debugger;
//   return total ? { ...current, child: total } : total;
// });
// console.log(result);

// var sum = arr.reduce((x, y) => x + y, 0);
// var mul = arr.reduce((x, y) => x * y, 1);
// console.log(sum); //求和，10
// console.log(mul); //求乘积，24

// let arr = [1, 2, 3, 4, 4, 1];
// const resultArr = arr.reduce((pre, curr) => {
//   if (!pre.includes(curr)) {
//     pre.push(curr);
//   }
//   return pre;
// }, []);
// console.log(resultArr);

// let arr = [
//   [0, 1],
//   [2, 3],
//   [4, 5],
// ];
// let newArr = arr.reduce((pre, cur) => {
//   return pre.concat(cur);
// }, []);
// console.log(newArr); // [0, 1, 2, 3, 4, 5]
// var arr = [1, 2, 3, 4, 5];

// var reverseList = function (head) {
//   let prev = null;
//   let curr = head;
//   while (curr) {
//     const next = curr.next;
//     curr.next = prev;
//     prev = curr;
//     curr = next;
//   }
//   return prev;
// };

// console.log(reverseList(arr));

/**
 * 将数组转换为链表
 * @param array arr  需要转换的数组
 * @param int  type  转换的类型，0为单链表，1为循环链表
 * @return object    返回链表
 */
function array2List(arr, type = 0) {
  if (!arr.length) return null;
  let header = { val: arr[0], next: null };
  let obj = header;
  for (let i = 1; i < arr.length; i++) {
    obj.next = { val: arr[i], next: null };
    obj = obj.next;
  }
  if (type) obj.next = header;
  return header;
}

console.log(array2List([1, 2, 3, 4]));

const list = array2List([1, 2, 3, 4]);

function reverse(head) {
  let prev = null;
  let curr = head;
  while (curr) {
    const next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }
  return prev;
}

console.log(reverse(list));
