const moment = require("moment-timezone");
console.log(
  `[2021-03-10T07:28:18.554Z] [8mha:////4BULv4RnjOoKwMIwOAlIf7owJkUCF7J7Z7OcEyaww7OlAAAAox+LCAAAAAAAAP9tjTEOAiEURD9rLGwtPQSbmFgZK1tC4wmQRYQl/7PAult5Iq/mHSRuYuUkk8yb5r3esM4JTpQs9wZ7h1k7HsNo6+ITpf4WaOKerlwTZgqGSzNJ6sx5QUnFwBLWwErAxqAOlB3aAlvh1UO1QaFtLyXV7yigcd0AT2CimotK5Qtzgt197DLhz/NXAHMswPa1h/gBdMwOJ7wAAAA=[0m[Pipeline] echo
  `
    .replace(
      // eslint-disable-next-line no-control-regex
      /(\[8mha:).*(\[0m)|(\[.*\])/g,
      ""
    )
    .replace(/\[(.+?)Z\]/g, (word) => {
      return `[${moment
        .utc(
          // 截取掉中括号
          word.substring(1, word.length - 2)
        )
        .tz(moment.tz.guess())
        .format("YYYY-MM-DD HH:mm:ss")}]`;
    })
);
