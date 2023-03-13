#!/usr/bin/node
// script that prints a square
const size = parseInt(process.argv[2]);

if (!Number.isInteger(size)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < size) {
    let j = 0;
    let square = '';
    while (j < size) {
      square += 'X';
      j += 1;
    }
    console.log(square);
    i += 1;
  }
}
