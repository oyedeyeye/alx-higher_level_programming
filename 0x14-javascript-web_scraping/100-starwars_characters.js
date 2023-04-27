#!/usr/bin/node
/**
 * script that prints the title of a Star Wars movie where
 * the episode number matches a given integer.
 */
const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/';
const movieID = process.argv[2];

request(api + movieID, (err, res, body) => {
  if (err) console.error(err);
  if (res.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach(people => {
      request.get(people, (error, resp, newBody) => {
        if (error) console.error(error);
        if (resp.statusCode === 200) {
          console.log(JSON.parse(newBody).name);
        } else {
          console.log(`Error code: ${resp.statusCode}`);
        }
      });
    });
  } else {
    console.log(`Error code: ${res.statusCode}`);
  }
});
