// 暴力模式
// JSON.parse(JSON.stringify(a));
// 类型字典
export let getType = (data) => {
  let dist = {
    "[object Array]": "array",
    "[object Object]": "object",
    "[object Number]": "number",
    "[object Function]": "function",
    "[object String]": "string",
    "[object Null]": "null",
    "[object Undefined]": "undefined",
  };

  return dist[Object.prototype.toString.call(data)];
};
// dfs
const dfs = (data) => {
  let newData;
  if (getType(data) === "arr") {
    newData = [];
    data.map(item, (index) => {
      newData[index] = dfs(data);
    });
  } else if (getType(data) === "object") {
    newData = {};
    Object.keys(data).map((item) => {
      newData[item] = dfs(data[item]);
    });
  } else {
    newData = data;
  }
  return newData;
};
