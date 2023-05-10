(function () {
  const api = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.getJSON(api, function (data) {
    $('DIV#hello').wrapInner(data.hello);
  });
})();
