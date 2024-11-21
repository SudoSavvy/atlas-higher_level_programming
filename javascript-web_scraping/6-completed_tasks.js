#!/usr/bin/node
const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Send a GET request to the API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};

    // Iterate through the tasks
    tasks.forEach(task => {
      if (task.completed) {
        if (completedTasks[task.userId] === undefined) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId]++;
      }
    });

    // Print the result
    console.log(completedTasks);
  }
});
