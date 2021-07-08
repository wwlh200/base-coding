const p1 = new Promise((resolve, reject) => {
  resolve("hello");
})
  .then((result) => result)
  .catch((e) => e);

const p2 = new Promise((resolve, reject) => {
  resolve("world");
})
  .then((result1) => result1)
  .catch((e) => e);

Promise.race([p1, p2])
  .then(([result, result1]) => console.log(result + result1))
  .catch((e) => console.log(e));
// ["hello", Error: 报错了]
