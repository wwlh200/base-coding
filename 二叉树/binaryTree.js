// left right val
class Tree {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }

  insert(val) {
    if (val <= this.val) {
      if (!this.left) {
        this.left = new Tree(val);
      } else {
        this.left.insert(val);
      }
    } else {
      if (!this.right) {
        this.right = new Tree(val);
      } else {
        this.right.insert(val);
      }
    }
  }
}
