// 创造promise对象实例
// const promise = new Promise((resolve, reject) => {
//   // ...some codes
//   if (true) {
//     resolve(value);
//   } else {
//     reject(error);
//   }
// });

// function timeout(ms) {
//   return new Promise((resolve, reject) => {
//     debugger;
//     setTimeout(resolve, ms, "done");
//   });
// }

// timeout(10000).then((value) => {
//   console.log(value);
// });

// new Promise(function (resolve, reject) {
//   console.log("Promise1");
//   resolve();
// });

// const loadImage=(url)=>{
//     return new Promise(function(resolve,reject){
//         const img=new Image();
//         img.onload=function(){
//             resolve();
//         }
//         img.onerror=function(){
//             reject();
//         }
//         img.src=url
//     })

// }

