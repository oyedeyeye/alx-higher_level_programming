#!/usr/bin/node
/**
 * script that prints the title of a Star Wars movie where
 * the episode number matches a given integer.
 */
const request = require('request');
const fs = require('fs');
const API_URL = process.argv[2];
const filePath = process.argv[3];

request(API_URL, filePath, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    fs.writeFile(
      filePath,
      body,
      {
        encoding: 'utf-8',
        flag: 'w'
      },
      err => {
        if (err) {
          console.error(`{ Error: ${err.message}, errno: ${err.errno}, code: '${err.code}', syscall: '${err.syscall}', path: '${err.path}' }`);
        }
      }
    );
  } else {
    console.log(`Error code: ${res.statusCode}`);
  }
});
