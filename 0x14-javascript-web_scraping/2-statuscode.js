#!/usr/bin/node
/**
 * script that display the status code of a GET request.
 * The first argument is the URL to request (GET)
 * The status code must be printed like this: code: <status code>
 * You must use the module request
 */
const request = require('request');
const urlArg = process.argv[2];

request.get(urlArg).on('response', response => {
	console.log('code: ', response.statusCode);
});
