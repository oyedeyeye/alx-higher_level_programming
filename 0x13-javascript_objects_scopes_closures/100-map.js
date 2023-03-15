#!/usr/bin/node
const list = require('./100-data').list;

const newList = [...list].map(el => el * list.indexOf(el));
console.log(list);
console.log(newList);
