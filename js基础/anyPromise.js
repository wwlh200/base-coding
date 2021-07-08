const p1 = new Promise((resolve, reject) => {
  console.log(1);
  reject("王巽星是个王八蛋");
});

const p2 = new Promise((resolve, reject) => {
  console.log(2);
  resolve(p1);
});

p2.then((result) => {
  console.log(result);
}).catch((result) => {
  console.log(`1${result}`);
});
