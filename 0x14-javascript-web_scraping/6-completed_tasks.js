#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.error(err);
  if (res.statusCode === 200) {
    const toDo = JSON.parse(body);
    const completed = {};
    toDo.forEach(task => {
      if (task.completed === true) {
        task.userId in completed ? (completed[task.userId] += 1) : (completed[task.userId] = 1);
      }
    });
    console.log(completed);
  } else {
    console.log(`Error code: ${res.statusCode}`);
  }
});
