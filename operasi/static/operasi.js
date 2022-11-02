$(document).ready(function() {
  $('#tableJadwalDokter').DataTable({
    "ajax": {
        "url": "/operasi/json/",
        "dataSrc": ''
    },
    "remove":true,
    "searching": true,
    "ordering": true,
    "responsive": true,
    "columns": [
      {"data": "pk",
        render: function(data,type,row){
          return "<button onclick='hapusJadwal(" + data + ")' class='bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded'>Hapus</button>";
        }
      },
        {"data": "fields.usernameDokter"},
        {"data": "fields.usernamePasien"},
        {"data": "fields.tanggal"},
        {"data": "fields.jam"},
        {"data": "fields.keterangan"},
    ]
  }).columns.adjust()
    .responsive.recalc();


  $('#tableJadwalPasien').DataTable({
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
          window.location.href = "/operasi/";
        },
        error: function(){
          alert("Gagal menambahkan jadwal operasi!");
        } 
      });
});