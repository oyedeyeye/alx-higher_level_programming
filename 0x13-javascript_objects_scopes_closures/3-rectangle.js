#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      let j = 0;
      let row = '';
      while (j < this.width) {
        row += 'X';
        j += 1;
      }
      console.log(row);
      i += 1;
    }
  }
}

module.exports = Rectangle;
