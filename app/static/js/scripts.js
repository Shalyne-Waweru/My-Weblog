$(document).ready(function(){
  
  $('.close').click(function(){
    $(".alert").css("display", "none");
  })

  $('.pic-upload').hide();

  $('#change-profile-btn').click(function(){
    $('.pic-upload').toggle();
  })

  $('.upvote').click(function(){
    count = parseInt($('.like-count').text())+1;
    $('.like-count').text(count);
  })

  $('.downvote').click(function(){
    count = parseInt($('.dislike-count').text())+1;
    $('.dislike-count').text(count);
  })

});

// Add active class to the current button (highlight it)
var header = document.getElementById("nav-btns");
var btns = header.getElementsByClassName("link");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}
