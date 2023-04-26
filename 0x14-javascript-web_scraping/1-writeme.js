#!/usr/bin/node
/**
 * script that writes a string to a file.
 * The first argument is the file path
 * The second argument is the string to write
 * The content of the file must be written in utf-8
 * If an error occurred during while writing, print the error object
 */
const fs = require('fs');

fs.writeFile(
  process.argv[2],
  process.argv[3],
  {
    encoding: 'utf-8',
    flag: 'w'
  },
  err => {
    if (err) {
      console.error(`{ Error: ${err.message},
      errno: ${err.errno},
      code: '${err.code}',
      syscall: '${err.syscall}',
      path: '${err.path}' }`);
    }
  }
);
