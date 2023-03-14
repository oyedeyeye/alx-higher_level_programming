#!/usr/bin/node
// returns the reversed version of a list

exports.esrever = function (list) {
  const newList = [];
  list.forEach(element => {
    newList.unshift(element);
  });
  return newList;
};
