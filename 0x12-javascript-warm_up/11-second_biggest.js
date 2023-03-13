#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
function secondBiggest (arr) {
  if (arr === undefined || arr.length === 0) {
    return 0;
  } else if (arr.length === 1) {
    return 0;
  }
  const sortedArr = [...arr];
  sortedArr.sort((a, b) => b - a);
  return sortedArr[1];
}

const args = process.argv.slice(2);
console.log(secondBiggest(args));
