// 创建对象
let xhr;
/**
 * 为了应对所有的现代浏览器，包括 IE5 和 IE6，请检查浏览器是否支持 XMLHttpRequest 对象。
 * 如果支持，则创建 XMLHttpRequest 对象。如果不支持，则创建 ActiveXObject
 */
if (window.XMLHttpRequest) {
  xhr = new XMLHttpRequest();
} else {
  xhr = new ActiveXObject("Microsoft.XMLHTTP");
}

// 请求(规定请求的类型、URL 以及是否异步处理请求。)
xhr.open("GET", "xxx.txt", true);

// 响应
/**
readyState	
存有 XMLHttpRequest 的状态。从 0 到 4 发生变化。
0: 请求未初始化
1: 服务器连接已建立
2: 请求已接收
3: 请求处理中
4: 请求已完成，且响应已就绪
 */
xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    // 请求成功
    console.log(xhr.responseText);
  }
};
// 发送
/**
send(string)	
将请求发送到服务器。

string：仅用于 POST 请求
 */
xhr.send();
