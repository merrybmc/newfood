function sign_Out() {
  $.removeCookie("mytoken", { path: "/" });
  window.location.href = "/login";
}
