$(document).ready(function () {
  if (document.querySelector(".comment_Input1").value == "") {
    document.querySelector(".comment_Add1").style.backgroundColor = "#A2A8A9";
  }
  if (document.querySelector(".comment_Input1").value != "") {
    document.querySelector(".comment_Add1").style.Color = "#999999";
    document.querySelector(".comment_Add1").style.backgroundColor = "#ffffff";
  }
});
