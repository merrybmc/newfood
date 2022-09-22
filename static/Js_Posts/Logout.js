function Logout() {
  $.removeCookie("mytoken", { path: "/" });
  alert("로그아웃!");
  window.location.href = "/login";
}
