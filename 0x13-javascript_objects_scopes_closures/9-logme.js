#!/usr/bin/node

let count = 0;
exports.logMe = function (data) {
  console.log(`${count}: ${data}`);
  count++;
};
