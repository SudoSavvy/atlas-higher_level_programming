// Fetches and displays the name of the Star Wars character
$(document).ready(function () {
    const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
    $.get(url, function (data) {
      $('#character').text(data.name);
    });
  });
  