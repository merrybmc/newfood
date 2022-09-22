$(document).ready(function () {
  show_Comment_List1();
  show_Comment_List2();
  show_Comment_List3();
  show_Comment_List4();
  show_Comment_List5();
  show_Comment_List6();
  show_Comment_List7();
});
function show_Comment_List1() {
  $.ajax({
    type: "GET",
    url: "/comment_list1",
    data: {},
    success: function (response) {
      let rows = response["info"];
      for (let i = 0; i < rows.length; i++) {
        let comment = rows[i]["comment"];
        let temp_html = "";
        temp_html = `<li class="comments">
        <span class="itemText"><b>ID</b>&nbsp&nbsp ${comment}</span>
    </li>`;
        $(".comment_List1").append(temp_html);
      }
    },
  });
}

function show_Comment_List2() {
  $.ajax({
    type: "GET",
    url: "/comment_list2",
    data: {},
    success: function (response) {
      let rows = response["info"];
      for (let i = 0; i < rows.length; i++) {
        let comment = rows[i]["comment"];
        let temp_html = "";
        temp_html = `<li class="comments">
          <span class="itemText"><b>ID</b>&nbsp&nbsp ${comment}</span>
      </li>`;
        $(".comment_List2").append(temp_html);
      }
    },
  });
}

function show_Comment_List3() {
  $.ajax({
    type: "GET",
    url: "/comment_list3",
    data: {},
    success: function (response) {
      let rows = response["info"];
      for (let i = 0; i < rows.length; i++) {
        let comment = rows[i]["comment"];
        let temp_html = "";
        temp_html = `<li class="comments">
            <span class="itemText"><b>ID</b>&nbsp&nbsp ${comment}</span>
        </li>`;
        $(".comment_List3").append(temp_html);
      }
    },
  });
}

function show_Comment_List4() {
  $.ajax({
    type: "GET",
    url: "/comment_list4",
    data: {},
    success: function (response) {
      let rows = response["info"];
      for (let i = 0; i < rows.length; i++) {
        let comment = rows[i]["comment"];
        let temp_html = "";
        temp_html = `<li class="comments">
            <span class="itemText"><b>ID</b>&nbsp&nbsp ${comment}</span>
        </li>`;
        $(".comment_List4").append(temp_html);
      }
    },
  });
}

function show_Comment_List5() {
  $.ajax({
    type: "GET",
    url: "/comment_list5",
    data: {},
    success: function (response) {
      let rows = response["info"];
      for (let i = 0; i < rows.length; i++) {
        let comment = rows[i]["comment"];
        let temp_html = "";
        temp_html = `<li class="comments">
            <span class="itemText"><b>ID</b>&nbsp&nbsp ${comment}</span>
        </li>`;
        $(".comment_List5").append(temp_html);
      }
    },
  });
}

function show_Comment_List6() {
  $.ajax({
    type: "GET",
    url: "/comment_list6",
    data: {},
    success: function (response) {
      let rows = response["info"];
      for (let i = 0; i < rows.length; i++) {
        let comment = rows[i]["comment"];
        let temp_html = "";
        temp_html = `<li class="comments">
            <span class="itemText"><b>ID</b>&nbsp&nbsp ${comment}</span>
        </li>`;
        $(".comment_List6").append(temp_html);
      }
    },
  });
}

function show_Comment_List7() {
  $.ajax({
    type: "GET",
    url: "/comment_list7",
    data: {},
    success: function (response) {
      let rows = response["info"];
      for (let i = 0; i < rows.length; i++) {
        let comment = rows[i]["comment"];
        let temp_html = "";
        temp_html = `<li class="comments">
            <span class="itemText"><b>ID</b>&nbsp&nbsp ${comment}</span>
        </li>`;
        $(".comment_List7").append(temp_html);
      }
    },
  });
}

function save_bucket1() {
  let comment = $(".comment_Input1").val();

  $.ajax({
    type: "POST",
    url: "/comment_list1",
    data: { comment_give: comment },
    success: function (response) {},
  });
}

function save_bucket2() {
  let comment = $(".comment_Input2").val();

  $.ajax({
    type: "POST",
    url: "/comment_list2",
    data: { comment_give: comment },
    success: function (response) {},
  });
}

function save_bucket3() {
  let comment = $(".comment_Input3").val();

  $.ajax({
    type: "POST",
    url: "/comment_list3",
    data: { comment_give: comment },
    success: function (response) {},
  });
}

function save_bucket4() {
  let comment = $(".comment_Input4").val();

  $.ajax({
    type: "POST",
    url: "/comment_list4",
    data: { comment_give: comment },
    success: function (response) {},
  });
}

function save_bucket5() {
  let comment = $(".comment_Input5").val();

  $.ajax({
    type: "POST",
    url: "/comment_list5",
    data: { comment_give: comment },
    success: function (response) {},
  });
}

function save_bucket6() {
  let comment = $(".comment_Input6").val();

  $.ajax({
    type: "POST",
    url: "/comment_list6",
    data: { comment_give: comment },
    success: function (response) {},
  });
}

function save_bucket7() {
  let comment = $(".comment_Input7").val();

  $.ajax({
    type: "POST",
    url: "/comment_list7",
    data: { comment_give: comment },
    success: function (response) {},
  });
}
