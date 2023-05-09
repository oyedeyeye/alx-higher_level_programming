(function () {
  const api = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.getJSON(api, function (json) {
    $('DIV#character').wrapInner(json.name);
  });
})();
