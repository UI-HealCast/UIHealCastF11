$(document).ready(function() {
  $('#tableJadwal').DataTable({
    "ajax": {
        "url": "/operasi/json/",
        "dataSrc": ''
    },
    "searching": true,
    "ordering": true,
    "responsive": true,
    "columns": [
        {"data": "fields.usernameDokter"},
        {"data": "fields.usernamePasien"},
        {"data": "fields.tanggal"},
        {"data": "fields.jam"},
        {"data": "fields.keterangan"},
    ]
  }).columns.adjust()
    .responsive.recalc();
});

$(document).on("submit", "#tambah_jadwal", function (e) {
    e.preventDefault();
    var token = $("#tambah_jadwal").find('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
        url: "/operasi/add/",
        method: "POST",
        data: {
            pasien: $("#id_pasien option:selected").text(),
            tanggal: $("#id_tanggal").val(),
            jam: $("#id_jam").val(),
            keterangan: $("#id_keterangan").val(),
            csrfmiddlewaretoken: token
        },
        dataType: "json",
        success: function(){
          alert('Jadwal operasi berhasil ditambahkan!');
          window.location.href = "/operasi/";
        },
        error: function(){
          alert("Gagal menambahkan jadwal operasi!");
        } 
      });
});