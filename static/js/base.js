// Schyler Lowry
// CIS218
// 8/3/2023


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


// Max length and text remaining script
var maxLength = 140;
$("[id='id_body']").keyup(function() {
  var textlen = maxLength - $(this).val().length;
  $("[id='rchars']").text(textlen);
});



// Scrolls twit feed container back to top 
// doesn't refresh feed/page
var container = $('#top');
$("#btn-back-to-top").click(function () {
    
    $('#top').animate({
        scrollTop: 0
    }, 800);

});


// clears the text field if user hits cancel button
$('#btn-cancel-comment').click(function() {
    $('textarea').val('')
});



// When user opens modal, adds the twit id hash to the url
// ugly solution, and unnecessary, but I wanted to try something unfamiliar
// I wanted it to add "/comment" after the twit id
  $(document).ready(function(){
    $(window.location.hash).modal('show');
    $('a[data-bs-toggle="modal"]').click(function(){
        window.location.hash = $(this).attr('href');
    });
 });


let userProfileDetails = document.getElementById("userProfileDetails")

$('#userProfileButton').click(function() {
    if (userProfileDetails.textContent.includes("View")) {
        // console.log("it's in there")
        userProfileDetails.textContent = "Hide Details about"
    } else {
        userProfileDetails.textContent = "View Details about"
    }
    
    
    // console.log(userProfileDetails.textContent)
});