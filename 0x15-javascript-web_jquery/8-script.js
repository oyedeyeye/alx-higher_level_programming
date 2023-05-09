(function () {
  const api = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.getJSON(api, function (json) {
    for (const result of json.results) {
      $('UL#list_movies').append('<li>' + result.title + '</li>');
    }
  });
})();
