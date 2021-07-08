const func = async () => {
  const a = new Promise((resolve, reject) => {
    resolve(200);
  });

  const b = new Promise((resolve, reject) => {
    setTimeout(() => reject(500), 5000);
  });
  debugger;
  const c = await Promise.allSettled([a, b]);
};

func();
