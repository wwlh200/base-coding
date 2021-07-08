/**
 * 找数据规律：1 2 3 5 8, fib数列
 * fib数列 1 1 2 3 5 8 ...
 * 结束条件：n ===1 或者 n ===2
 * 缩小范围：n-1到n-2
 */
const step = (n) => {
  if (n <= 2) {
    return n;
  }
  return step(n - 1) + step(n - 2);
};
console.log(step(5));
