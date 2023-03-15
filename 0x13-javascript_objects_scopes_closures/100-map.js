#!/usr/bin/node
const list = require('./100-data').list;

const data = list;
const newList = data.map((el, index) => el * index);
console.log(data);
console.log(newList);
