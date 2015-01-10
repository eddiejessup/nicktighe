$(document).ready(function() {
    $(".fancybox").fancybox({
          helpers: {
              title : {
                  type : 'float'
              }
          }
      });

    $('#gallery').imagesLoaded(function() {
        $('#gallery').masonry({
          itemSelector: '.img'
        });
    });
});
