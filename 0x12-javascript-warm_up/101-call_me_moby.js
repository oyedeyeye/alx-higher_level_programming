#!/usr/bin/node
// function that executes x times a function
function callMeMoby(x, theFunction) {
	let i = 0;
	while (i < x) {
		theFunction();
		i += 1;
	}
}

module.exports = { callMeMoby };
