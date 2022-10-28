$(document).ready(function () {
    loadData();
});


$(document).on("submit", "#tembakDB", function (e) {
e.preventDefault();
$.ajax({
  type: "POST",
  url: "/modif-hasil/",
  data: {
    hasil: $("#hasil").val(),
    peka : document.getElementById("tembakDB").getAttribute("class"),
  },
  dataType: "json",
  success: function () {

    alert("Data berhasil ditambahkan");
    document.location.href = '/menu-pasien'

  },
});
});