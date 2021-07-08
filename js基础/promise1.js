const PENDING = "pending";
const FULFILLED = "fulfilled";
const REJECTED = "rejected";

class CustomPromise {
  // 执行器
  constructor(executor) {
    //当前函数this指定CustomPromise对象
    this.resolve = this.resolve.bind(this);
    this.reject = this.reject.bind(this);

    // 初始状态、成功返回数据、失败返回原因
    this.status = PENDING;
    this.value = undefined;
    this.reason = undefined;

    //异步处理时因为需要等待 所以要存储成功回调函数与失败回调，所以采用数组
    this.successCallback = [];
    this.failCallback = [];

    // 执行执行器
    executor(this.resolve, this.reject);
  }

  // 执行成功的回调
  resolve(value) {
    // 因为状态只能是pending=> fulfilled/rejected 如果其他状态就返回
    if (this.status !== PENDING) return;
    // 执行之后状态更改为fulfilled
    this.status = FULFILLED;
    // 将成功的值返回
    this.value = value;

    // 判断方法是否存在并且执行成功回调方法
    while (this.successCallback.length > 0) {
      this.successCallback.shift()(this.value);
    }
  }

  // 执行失败的回调
  reject(reason) {
    if (this.status !== PENDING) return;
    this.status = REJECTED;
    this.reason = reason;

    // 判断方法是否存在并且执行成功回调方法
    while (this.failCallback.length > 0) {
      this.failCallback.shift()(this.reason);
    }
  }

  // then方法执行
  then(successCallback, failCallback) {
    switch (this.status) {
      case FULFILLED:
        successCallback(this.value);
        break;
      case REJECTED:
        failCallback(this.reason);
        break;
      default:
        // 变量记录当前的回调方法，存在异步的执行顺序
        // CustomPromise声明=》then方法的调用=》异步函数返回值调用resolve/reject方法
        this.successCallback.push(successCallback);
        this.failCallback.push(failCallback);
        break;
    }
  }

  catch(failCallback) {
    failCallback(this.reason);
  }
}

// 总结：有异步的情况，先执行then方法，但是此时状态还是pending，就将回调方法记录下来，等resolve执行的时候，再执行回调方法

let promise = new CustomPromise((resolve, reject) => {
  setTimeout(() => {
    setTimeout(() => {
      resolve("成功");
    }, 3000);
  }, 3000);
  //reject('失败');
});
promise.then(
  (val) => {
    console.log(val);
  },
  (reason) => {
    console.log(reason);
  }
);
