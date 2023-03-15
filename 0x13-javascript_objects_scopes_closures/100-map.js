#!/usr/bin/node
const list = require('./100-data').list;

const data = list;
const newList = data.map(el => el * data.indexOf(el));
console.log(data);
console.log(newList);
