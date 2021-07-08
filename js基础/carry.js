const sum = (a, b, c, d) => {
  return a + b + c + d;
};

console.log(sum(1, 2, 3, 4));

const sum1 = (a, b) => {
  return (c, d) => {
    return a + b + c + d;
  };
};

const abSum = sum1(1, 2);

console.log(abSum(3, 4));

console.log({ a: 1, ...{ b: undefined } });
