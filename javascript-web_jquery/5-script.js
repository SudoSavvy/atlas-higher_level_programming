// Adds a new <li> element to the UL.my_list when the user clicks on DIV#add_item
$(document).ready(function () {
    $('#add_item').click(function () {
      $('.my_list').append('<li>Item</li>');
    });
  });
  