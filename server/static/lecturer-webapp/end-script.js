$(document).ready(function () {

  // Sign out on button press
  $("#sign-out-button").click(function () {
    document.cookie = "cuas_lecturer_login_session=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/lecturer/;";
    window.location.replace("lecturer/login");
  });

  // Change focus navbar colours on click
  $(".nav a").on("click", function () {
    $(".nav").find(".active").removeClass("active");
    $(this).addClass("active");
  });

});