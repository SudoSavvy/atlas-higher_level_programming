// Fetches the "hello" translation and displays it in the #hello div
$(document).ready(function () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
  