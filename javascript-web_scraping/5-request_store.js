#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Send a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // Write the body of the response to the specified file
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
