#!/usr/bin/node
const args = process.argv.slice(2);
const intArg = parseInt(args[0]);
if (Number.isInteger(intArg)) {
  console.log('My number: ' + intArg);
} else {
  console.log('Not a number');
}
