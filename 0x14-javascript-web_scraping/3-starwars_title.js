#!/usr/bin/node
/**
 * script that prints the title of a Star Wars movie where
 * the episode number matches a given integer.
 */
const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/';
const episodeNum = process.argv[2];

request(api + episodeNum, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const resJSON = JSON.parse(body);
    console.log(resJSON.title);
  } else {
    console.log(`Error code: ${res.statusCode}`);
  }
});
