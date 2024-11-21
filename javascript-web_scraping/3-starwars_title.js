#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Send a GET request to the API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
