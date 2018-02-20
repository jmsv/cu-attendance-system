// Change focus navbar colours on click
$(".nav a").on("click", function () {
  $(".nav").find(".active").removeClass("active");
  $(this).addClass("active");
});

// Get session ID cookie
function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}
var sessionId = getCookie("cuas_lecturer_login_session");

function goToLogin() {
  window.location.replace("lecturer-login")
}
// If there's no session cookie, log in
if (!sessionId) goToLogin();

// Check login session is valid.
// This calls the back end to check login is valid. If not, redir to log in
var url = "api/lecturer-session-check?session=" + sessionId;
$.get(url, function (data) {
  if (!data['data']['logged_in']) goToLogin();
}).fail(function () {
  goToLogin();
});