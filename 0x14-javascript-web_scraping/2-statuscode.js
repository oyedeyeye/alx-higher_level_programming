#!/usr/bin/env node
/**
 * script that display the status code of a GET request.
 * The first argument is the URL to request (GET)
 * The status code must be printed like this: code: <status code>
 * You must use the module request
 */
const request = require('request');
const urlArg = process.argv[2];

request(urlArg, (error, response) => {
	if (error) {
		console.error(error);
		throw error;
	}
	console.log('code: ', response && response.statusCode);
});
