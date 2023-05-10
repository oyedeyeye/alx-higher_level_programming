$('document').ready(function () {
  $('INPUT#btn_translate').on('click', translate);
  $('INPUT#btn_translate').on('focus', function () {
    $(this).on('keypress', function (e) {
      if (e.which === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const api = 'https://fourtonfish.com/hellosalut/hello';
  $.get(api + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  }
  );
}
