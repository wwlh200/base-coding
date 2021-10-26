/**
 * fib数列 1 1 2 3 5 8 ...
 * 结束条件：n ===1 或者 n ===2
 * 缩小范围：n-1到n-2
 */

const fib = (n) => {
  if (n <= 2) {
    return n;
  }
  return fib(n - 1) + fib(n - 2);
};

console.log(fib(6));
