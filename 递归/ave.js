/**
 *
 *
 * 结束条件：n=1 n=2
 * 缩小范围：n*fn(n-1)
 */
const ave = (n) => {
  if (n <= 2) {
    return n;
  }
  return n * ave(n - 1);
};

const ave2 = (n) => {
  if (n <= 2) {
    return n;
  }
  let sum = 1;
  while (n > 0) {
    sum = sum * n;
    n--;
  }
  return sum;
};

console.log(ave(5));
