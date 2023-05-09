(function () {
  const api = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const greet = 'hello';
  $.getJSON(api, { data: greet }, function (data) {
    $('DIV#hello').wrapInner(data.value);
  });
})();
