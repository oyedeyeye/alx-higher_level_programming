#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);
const newList = list.map(el => el * list.indexOf(el));
console.log(newList);
