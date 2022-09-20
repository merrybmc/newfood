$(document).ready(function () {
  show_order();
});

function show_order() {
  " ";
}

{
  $.ajax({
    type: "GET",
    url: "/order",
    data: {},
    success: function (response) {
      const one_p = response["one_p"];
      const one_src = response["one_is"];

      const two_p = response["two_p"];
      const two_src = response["two_is"];

      const three_p = response["three_p"];
      const three_src = response["three_is"];

      const four_p = response["four_p"];
      const four_src = response["four_is"];

      const five_p = response["five_p"];
      const five_src = response["five_is"];

      const six_p = response["six_p"];
      const six_src = response["six_is"];

      const seven_p = response["seven_p"];
      const seven_src = response["seven_is"];

      const p1 = document.querySelector(".one_p");
      const src1 = document.querySelector(".one_src");
      const p2 = document.querySelector(".two_p");
      const src2 = document.querySelector(".two_src");
      const p3 = document.querySelector(".three_p");
      const src3 = document.querySelector(".three_src");
      const p4 = document.querySelector(".four_p");
      const src4 = document.querySelector(".four_src");
      const p5 = document.querySelector(".five_p");
      const src5 = document.querySelector(".five_src");
      const p6 = document.querySelector(".six_p");
      const src6 = document.querySelector(".six_src");
      const p7 = document.querySelector(".seven_p");
      const src7 = document.querySelector(".seven_src");

      const p1_item = document.createElement("b");
      const p1_src = document.createElement("img");
      const p2_item = document.createElement("b");
      const p2_src = document.createElement("img");
      const p3_item = document.createElement("b");
      const p3_src = document.createElement("img");
      const p4_item = document.createElement("b");
      const p4_src = document.createElement("img");
      const p5_item = document.createElement("b");
      const p5_src = document.createElement("img");
      const p6_item = document.createElement("b");
      const p6_src = document.createElement("img");
      const p7_item = document.createElement("b");
      const p7_src = document.createElement("img");

      p1_item.innerHTML = one_p;
      p2_item.innerHTML = two_p;
      p3_item.innerHTML = three_p;
      p4_item.innerHTML = four_p;
      p5_item.innerHTML = five_p;
      p6_item.innerHTML = six_p;
      p7_item.innerHTML = seven_p;

      p1_src.setAttribute("src", one_src);
      p1_src.setAttribute("class", "card-img-top");
      p1_src.setAttribute("alt", "빈 이미지");

      p2_src.setAttribute("src", two_src);
      p2_src.setAttribute("class", "card-img-top");
      p2_src.setAttribute("alt", "빈 이미지");

      p3_src.setAttribute("src", three_src);
      p3_src.setAttribute("class", "card-img-top");
      p3_src.setAttribute("alt", "빈 이미지");

      p4_src.setAttribute("src", four_src);
      p4_src.setAttribute("class", "card-img-top");
      p4_src.setAttribute("alt", "빈 이미지");

      p5_src.setAttribute("src", five_src);
      p5_src.setAttribute("class", "card-img-top");
      p5_src.setAttribute("alt", "빈 이미지");

      p6_src.setAttribute("src", six_src);
      p6_src.setAttribute("class", "card-img-top");
      p6_src.setAttribute("alt", "빈 이미지");

      p7_src.setAttribute("src", seven_src);
      p7_src.setAttribute("class", "card-img-top");
      p7_src.setAttribute("alt", "빈 이미지");

      p1.appendChild(p1_item);
      src1.appendChild(p1_src);
      p2.appendChild(p2_item);
      src2.appendChild(p2_src);
      p3.appendChild(p3_item);
      src3.appendChild(p3_src);
      p4.appendChild(p4_item);
      src4.appendChild(p4_src);
      p5.appendChild(p5_item);
      src5.appendChild(p5_src);
      p6.appendChild(p6_item);
      src6.appendChild(p6_src);
      p7.appendChild(p7_item);
      src7.appendChild(p7_src);
    },
  });
}
