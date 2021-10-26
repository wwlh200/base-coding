const arr = [];
let i = 0;
while (arr.length < 5) {
  const num = Math.floor(Math.random() * 10);
  if (!arr.find((item) => item === num)) {
    arr.push(num);
  }
}

console.log(arr);
