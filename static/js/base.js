$(document).ready(function () {
    $(".like_button").click(function (event) {
        // The work we want to do on click.

        // Get required data
        let target = $(event.currentTarget);
        let twit_id = target.data('id');
        let twit_action = target.data('action');
        let twit_like_url = target.data('like-url');

        // Get icon and count elements
        let like_icon = target.find('.like_icon');
        let like_count = target.find('.like_count');

        $.ajax({
            url: twit_like_url,
            data: {
                twit_id: twit_id,
                twit_action: twit_action,
            },
        }).done(function (data) {
            // Do completion work here.
            if (data.success) {
                if (twit_action === 'like') {
                    // Do like
                    target.removeClass('btn-outline-primary');
                    target.addClass('btn-primary');
                    like_icon.removeClass('bi-hand-thumbs-up');
                    like_icon.addClass('bi-hand-thumbs-up-fill');
                    like_count.html(Number(like_count.html()) + 1);
                    target.data('action', 'unlike');
                } else {
                    //Do unlike
                    target.removeClass('btn-primary');
                    target.addClass('btn-outline-primary');
                    like_icon.removeClass('bi-hand-thumbs-up-fill');
                    like_icon.addClass('bi-hand-thumbs-up');
                    like_count.html(Number(like_count.html()) - 1);
                    target.data('action', 'like');
                }
            }
        });
    });
});



// var maxLength = 140;
// $('textarea').keyup(function() {
//   var textlen = maxLength - $(this).val().length;
//   $('#rchars').text(textlen);
// });


var maxLength = 140;
$("[id='id_body']").keyup(function() {
  var textlen = maxLength - $(this).val().length;
  $("[id='rchars']").text(textlen);
});


var container = $('#top');
$("#btn-back-to-top").click(function () {
    
    $('#top').animate({
        scrollTop: 0
    }, 800);

});




// source: mdBootstrap
let mybutton = document.getElementById("btn-back-to-top");
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}


$('#btn-cancel-comment').click(function() {
    $('textarea').val('')
});

$('#openModal').on('loaded.bs.modal', function () {
    if (typeof (history.pushState) != "undefined") {
          var obj = { Title: "Testing", Url: 'testing/1/' };
          history.pushState(obj, obj.Title, obj.Url);
      }
  })

  $(document).ready(function(){
    $(window.location.hash).modal('show');
    $('a[data-bs-toggle="modal"]').click(function(){
       window.location.hash = $(this).attr('href');
    });
 });

 $(document).ready(function () {
    var hash = window.location.hash; // #modal-1
    $(hash).modal('toggle');
  });
  
  
  $(document).on('show.bs.modal', ".modal", function(event) {
    window.location.hash = 'blah' // event.currentTarget.id;
  });