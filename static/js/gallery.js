$('#gallery').imagesLoaded(function() {
    $('#gallery').masonry({
      itemSelector: '.img'
    });
});

$(document).ready(function() {
    $(".fancybox").fancybox({
          helpers: {
              title : {
                  type : 'float'
              }
          }
      });
});
