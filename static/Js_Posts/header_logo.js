$(document).ready(function () {
  $(".header_Logo").mouseover(function () {
    $(this).attr(
      "src",
      "https://w.namu.la/s/5a0dfbc22d0e432def0ab164c2f53441794f55e17f00ce84ab021bea2dae11d2c0d93adbfd509f1f4fc1476d32fa854b7b3d0d58ba9d0fbad8b57f2280d6d33005531e674db993c057cdb93614b899719f31bc1bcee896d23661b369e31f091c"
    );
  });

  $(".header_Logo").mouseout(function () {
    $(this).attr(
      "src",
      "https://blogpfthumb-phinf.pstatic.net/MjAyMTA3MTZfMjM1/MDAxNjI2NDM5OTI4OTY1.2x609TV3FY7cLyh_Qh_AzL2_-pKwlVMn7xWlF3zq5H8g.pZwJumYC8UH4LRdqYKmVo0CzhmVzXKRHXKs6UYZw8Hkg.PNG.choibongae/pepe-licks-lips.png?type=w161"
    );
  });

  const logo_Top = document.querySelector(".header_Logo");

  logo_Top.onclick = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };
});
