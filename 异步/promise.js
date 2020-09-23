/*
const promise = new Promise((resolved, rejected) => {
  if (//异步操作成功) {
    resolved(value); // 将Promise对象的状态从“未完成”变为“成功”（即从 pending 变为 resolved），在异步操作成功时调用，并将异步操作的结果，作为参数传递出去；
  } else {
    rejected(error); // 将Promise对象的状态从“未完成”变为“失败”（即从 pending 变为 rejected），在异步操作失败时调用，并将异步操作报出的错误，作为参数传递出去。
  }
});
*/

// 可以用then方法分别指定resolved状态和rejected状态的回调函数。
promise.then(value=>{

}).catch(error=>{

});

/*
then方法可以接受两个回调函数作为参数。
第一个回调函数是Promise对象的状态变为resolved时调用
第二个回调函数是Promise对象的状态变为rejected时调用。
其中，第二个函数是可选的，不一定要提供。这两个函数都接受Promise对象传出的值作为参数。
*/