class Publisher {
  constructor() {
    this.subscriber = [];
  }

  add(sub) {
    this.subscriber.push(sub);
  }

  notify(mas) {
    this.subscriber.map((item) => {
      item.update(mas + "中国崛起了");
    });
  }
}

class Subscriber {
  constructor(name) {
    this.name = name;
  }

  update(msg) {
    console.log(`${this.name}---${msg}`);
  }
}

const sub1 = new Subscriber("张飞");
const sub2 = new Subscriber("赵云");

const publisher = new Publisher();

publisher.add(sub1);
publisher.add(sub2);

publisher.notify("王巽星");
