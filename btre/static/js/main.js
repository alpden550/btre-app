const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(
  function () {
    $('#form-error').fadeOut('slow');
  }, 5000
);

setTimeout(
  function () {
    $('#message').fadeOut('slow');
  }, 5000
);
