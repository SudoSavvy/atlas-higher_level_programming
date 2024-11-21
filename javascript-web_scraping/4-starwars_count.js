#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Send a GET request to the API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    // Loop through each film and check for Wedge Antilles' presence
    films.forEach((film) => {
      if (film.characters.some((char) => char.includes('/18/'))) {
        count++;
      }
    });

    console.log(count);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
