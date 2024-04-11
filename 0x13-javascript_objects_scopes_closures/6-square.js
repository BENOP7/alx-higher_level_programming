#!/usr/bin/node

const Base = require('./5-square');

module.exports = class Square extends Base {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c) {
          process.stdout.write(c);
        } else {
          process.stdout.write('X');
        }
      }
      process.stdout.write('\n');
    }
  }
};
