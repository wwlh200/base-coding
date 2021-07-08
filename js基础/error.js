Promise.try(function () {
  new Promise((resolve, reject) => {
    resolve("王巽星我孙子呢");
  });
}).then((value) => {
  const a = 1;
  a = 2;
  console.log(value);
});
