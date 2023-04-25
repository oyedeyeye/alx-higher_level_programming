#!/usr/bin/node
/**
 * script that reads and prints the content of a file.
 * The first argument is the file path
 * The content of the file must be read in utf-8
 * If an error occurred during the reading, print the error object
 */
const fs = require('fs');
const myFile = `${process.argv[2]}`;

fs.readFile(myFile, 'utf-8', (err, data) => {
  if (err) {
    console.error(`{ Error: ${err.message},
      errno: ${err.errno},
      code: '${err.code}',
      syscall: '${err.syscall}',
      path: '${err.path}' }`);
    return;
  }
  console.log(data);
});
