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
      this.successCallback.shift()();
    }
  }

  // 执行失败的回调
  reject(reason) {
    if (this.status !== PENDING) return;
    this.status = REJECTED;
    this.reason = reason;

    // 判断方法是否存在并且执行成功回调方法
    while (this.failCallback.length > 0) {
      this.failCallback.shift()();
    }
  }

  // then方法执行
  then(successCallback, failCallback) {
    let promise2 = new CustomPromise((resolve, reject) => {
      switch (this.status) {
        case FULFILLED:
          //settimeout 宏任务，会在当前所有同步任务完成之后执行回调函数内容 这时候 promise2已经实例化完毕可以调用
          setTimeout(() => {
            let result = successCallback(this.value);
            this.resolvePromise(promise2, result, resolve, reject);
          }, 0);

          break;
        case REJECTED:
          setTimeout(() => {
            let result = failCallback(this.reason);
            this.resolvePromise(promise2, result, resolve, reject);
          }, 0);
          break;
        default:
          //变量记录当前的回调方法  存在异步的执行顺序
          //MyPromise声明 => then方法的调用 => 异步函数返回值调用resolve/reject方法
          //把当前回调函数添加到数组中
          this.successCallback.push(() => {
            setTimeout(() => {
              let result = successCallback(this.value);
              this.resolvePromise(promise2, result, resolve, reject);
            }, 0);
          });
          this.failCallback.push(() => {
            setTimeout(() => {
              let result = failCallback(this.reason);
              this.resolvePromise(promise2, result, resolve, reject);
            }, 0);
          });
          break;
      }
    });
    return promise2;
  }

  // 同时我们定义一个方法 判断当前then的返回值使普通值还是promise函数
  resolvePromise(promise2, result, resolve, reject) {
    if (promise2 === result) {
      return reject(
        new TypeError("Chaining cycle detected for pormise #<Promise>")
      );
    }
    // 判断当前返回值是promise对象
    if (result instanceof CustomPromise) {
      result.then(resolve, reject);
    } else {
      resolve(result);
    }
  }

  catch(failCallback) {
    failCallback(this.reason);
  }

  static all(arr) {
    return new CustomPromise((resolve, reject) => {
      let result = [];
      let index = 0;
      function addData(key, value) {
        result[key] = value;
        index++;
        if (index === arr.length) resolve(result);
      }
      for (let i = 0; i < arr.length; i++) {
        if (arr[i] instanceof CustomPromise) {
          //调用对象的then方法，把成功回调值插入返回数组，如果失败，则返回错误原因。
          arr[i].then(
            (value) => {
              addData(i, value);
            },
            (reason) => {
              reject(reason);
            }
          );
        } else {
          //普通值直接插入
          addData(i, arr[i]);
        }
      }
    });
  }

  static race(arr) {
    return new CustomPromise((resolve, reject) => {
      for (let i = 0; i < arr.length; i++) {
        let current = arr[i];
        if (current instanceof CustomPromise) {
          //调用对象的then方法，把成功回调值插入返回数组，如果失败，则返回错误原因。
          current.then(resolve, reject);
        } else {
          //普通值直接插入
          resolve(current);
        }
      }
    });
  }
}

// 总结：有异步的情况，先执行then方法，但是此时状态还是pending，就将回调方法记录下来，等resolve执行的时候，再执行回调方法

let promise1 = new CustomPromise((resolve, reject) => {
  setTimeout(() => {
    resolve("成功1");
  }, 2000);
});
let promise2 = new CustomPromise((resolve, reject) => {
  setTimeout(() => {
    resolve("成功2");
  }, 3000);
});

CustomPromise.all([promise1, promise2, "王巽星我儿子"]).then((value) =>
  console.log(value)
);
