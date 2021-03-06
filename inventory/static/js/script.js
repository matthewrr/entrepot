$("#category").change(function () {
  var category = $(this).val();
  console.log(category);
  var category_upper = category[0].toUpperCase() + category.slice(1);

  $.ajax({
    url: '/ajax/item_categories/',
    data: {'category': category},
    dataType: 'json',
    success: function (response) {
        len = Object.keys(response).length;
        var target = $("#subcategory");
        target.empty();
        if (len == 0 ) {
          if (!$(target).attr( "disabled" )) {
            target.prop("disabled", true);
          }
          target.append(`<option class='subcategory' value='${category}'>No ${category_upper}s Exist</option>`);
        } else {
          target.prop("disabled", false);
          target.append(`<option class='subcategory' value='${category}'>Select a ${category_upper}:</option>`);
          for (obj in response) { 
            $("#subcategory").append(`<option class='subcategory' value='${response[obj]}'>${response[obj]}</option>`);
          }
        }
    }
  });

});