const a = {};
const b = new Map();

a[2] = "aa";
a[3] = "bb";
a["22"] = "bb";
a["222"] = "bb";
a[1] = "cc";
a[4] = "dd";

b.set(2, "aa");
b.set(3, "bb");
b.set("22", "bb");
b.set("222", "bb");
b.set(1, "cc");
b.set(4, "dd");
console.log(a);
console.log(b);

const removeArrayFromAll = (currentArr, allArr) => {
  currentArr.forEach((item) => {
    allArr.splice(
      allArr.findIndex((v) => v === item),
      1
    );
  });
  return allArr;
};

console.log(removeArrayFromAll([7, 3, 4], [1, 2, 3, 4, 5, 6, 7]));
