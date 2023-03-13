#!/usr/bin/node
// script that prints a message depending of the number of arguments passed:
const argLength = process.argv.length;

if (argLength > 2) {
  if (argLength > 3) {
    console.log('Arguments found');
  } else {
    console.log('Argument found');
  }
} else {
  console.log('No argument');
}
