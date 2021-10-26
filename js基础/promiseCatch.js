// new Promise((resolve, reject) => {
//   //   reject("王巽星我儿子");
//   throw new Error("王巽星我孙子呢");
// }).catch((v) => {
//   console.log(v);
// });

// // 写法一
// const promise = new Promise(function(resolve, reject) {
//     try {
//       throw new Error('test1');
//     } catch(e) {debugger
//       reject(e);
//     }
//   });
//   promise.catch(function(error) {debugger
//     console.log(error);
//   });
  
  // 写法二
//   const promise = new Promise(function(resolve, reject) {
//     reject(new Error('test2'));
//   });
//   promise.catch(function(error) {
//     console.log(error);
//   });

const someAsyncThing = function() {
    return new Promise(function(resolve, reject) {
      // 下面一行会报错，因为x没有声明
      resolve(2);
    });
  };
  
  someAsyncThing().then(function() {
    console.log('everything is great');
  });
  
  setTimeout(() => { console.log(123) }, 1000);