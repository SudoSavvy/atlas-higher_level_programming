// Fetches and lists all the movie titles
$(document).ready(function () {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    $.get(url, function (data) {
      data.results.forEach(function (movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    });
  });
  