#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  const nb = number + 1;
  theFunction(nb);
}

module.exports = { addMeMaybe };
