#!/usr/bin/node
// returns the number of occurrences in a list:

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(el => {
    if (el === searchElement) {
      count += 1;
    }
  });
  return count;
};
