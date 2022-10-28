$(document).ready(function () {
    $.ajax({
        url: "/operasi/json/",
        method: "GET",
        dataType: "json",
        success: function(data){
          var table = $('#tableJadwal');
          table.empty();
          if (data == '') {
            table.append("<div class='flex justify-center bg-yellow-300 p-3 rounded-2xl'>" +
            "<p>Tidak ada jadwal operasi!</p></div>");
          } else {
            table.append("<table class='table-auto'><thead><tr><th>Dokter</th>"+
              "<th>Pasien</th><th>Tanggal</th>"+
              "<th>Jam</th><th>Keterangan</th>"+
              "</tr></thead><tbody>");
            $(data).each(function(key, val){
                table.append("<tr><td>"+val.fields.dokter+"</td><td>"+
                                        val.fields.pasien+"</td><td>"+
                                        val.fields.tanggal+"</td><td>"+
                                        val.fields.jam+"</td><td>"+
                                    +val.fields.keterangan+"</td></tr>");
            });
            table.append("</tbody></table>");
          }
        },
        error: function(error){
          alert(error);
        }
    })
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
          console.log($("#id_pasien option:selected").text());
          console.log($("#id_tanggal").val());
          console.log($("#id_jam").val());
          console.log($("#id_keterangan").val());
          alert("Gagal menambahkan jadwal operasi!");
        } 
      });
});