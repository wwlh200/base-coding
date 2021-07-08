function promiseAjax(url) {
  return new Promise((resolve, reject) => {
    let xhr;
    if (window.XMLHttpRequest) {
      xhr = new XMLHttpRequest();
    } else {
      xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhr.open("GET", url, true);
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        // 请求成功
        console.log(xhr.responseText);
        resolve(xhr.responseText);
      } else {
        reject("出错了嘛！");
      }
    };
    xhr.send();
  });
}

promiseAjax("/posts.json").then(
  function (json) {
    console.log("Contents: " + json);
  },
  function (error) {
    console.error("出错了", error);
  }
);
