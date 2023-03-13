#!/usr/bin/node
// script that computes and prints a factorial
function factorial (num) {
  const n = parseInt(num);
  if (isNaN(n)) {
    return 1;
  } else if (n < 2) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const newArg = process.argv[2];
console.log(factorial(newArg));
