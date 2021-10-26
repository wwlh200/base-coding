var tag = 0;
function test1() {
  return tag;
}
function test2(tag) {
  tag = 1;
  return;
  tag;
}
function test3() {
  return test2();
}
console.log(test3());
console.log(test2());
console.log(test1());
