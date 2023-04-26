#!/usr/bin/node
/**
 * script that prints the title of a Star Wars movie where
 * the episode number matches a given integer.
 */
const request = require('request');
const API_URL = process.argv[2];

request(API_URL, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const results = JSON.parse(body).results;
    let count = 0;
    results.forEach(el => {
      el.characters.forEach(char => {
        if (char.endsWith('/18/')) {
          count += 1;
        }
      });
    });
    console.log(count);
  } else {
    console.log(`Error code: ${res.statusCode}`);
  }
});
