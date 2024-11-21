#!/usr/bin/node
const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Send a GET request to the URL
request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
