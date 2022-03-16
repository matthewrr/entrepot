$("#category").change(function () {
  var category = $(this).val();
  var category_upper = category[0].toUpperCase() + category.slice(1);

  $.ajax({
    url: '/ajax/item_categories/',
    data: {'category': category},
    dataType: 'json',
    success: function (response) {
        var target = $("#secondary-dropdown");
        target.empty();
        target.prop("disabled", false);
        target.append(`<option class='secondary-value' value='lalalalla'>Select a ${category_upper}:</option>`);
        for (obj in response) {
          $("#secondary-dropdown").append(`<option class='secondary-value' value='lalalalla'>${response[obj]}</option>`);
      }
    }
  });

});