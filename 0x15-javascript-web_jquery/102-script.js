$('document').ready(function () {
  const api = 'https://fourtonfish.com/hellosalut/hello';
  $('INPUT#btn_translate').click(function () {
    $.get(api + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    }
    );
  });
});
