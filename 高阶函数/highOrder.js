// 常规函数实现
const consoleA = () => {
  console.log("我们都一样");
  console.log("A");
};

const consoleB = () => {
  console.log("我们都一样");
  console.log("B");
};

consoleA();
consoleB();
// 高阶函数（高阶函数就是一个函数，且该函数接受一个函数作为参数，并返回一个新的函数。利用装饰器模式）实现
const consoleAA = () => {
  console.log("AA");
};

const consoleBB = () => {
  console.log("BB");
};
const wrapConsole = (consoleFunc) => {
  return () => {
    console.log("我们都一样");
    consoleFunc();
  };
};

wrapConsole(consoleAA)();
wrapConsole(consoleBB)();
