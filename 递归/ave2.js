/**
 * 结束条件n=1,n=2
 * 缩小范围 fn(n)*fn(n-1)
 *
 */
const ave = (n) => {
  if (n === 1 || n === 2) {
    return n;
  }
  return n * ave(n - 1);
};

const ave2 = (n) => {
  let sum = 1;
  while (n > 1) {
    sum *= n;
    n--;
  }
  return sum;
};
console.log(ave2(4));
