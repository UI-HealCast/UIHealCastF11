$(document).ready(function () {
    $.ajax({
        url: "/operasi/json/",
        method: "GET",
        dataType: "json",
        success: function(data){
          var table = $('#tableJadwal');
          table.empty();
          if (data == '') {
            table.append("<p>Tidak ada jadwal operasi!</p>");
          } else {
            table.append("<table class='table-auto'><thead><tr><th>Dokter</th>"+
              "<th>Pasien</th><th>Tanggal</th>"+
              "<th>Jam</th><th>Keterangan</th>"+
              "</tr></thead><tbody>");
            $(data).each(function(key, val){
            table.append("<tr><td>"+val.fields.dokter.username+"</td><td>"+
              val.fields.pasien.username+"</td><td>"+
              val.fields.tanggal+"</td><td>"+val.fields.jam+"</td><td>"+
              +val.fields.keterangan+"</td></tr>")
            })
            table.append("</tbody></table>");
            if (adalahDokter){
              table.append("<button type='button'>Click Me!</button>")
            } 
          }
        },
        error: function(error){
          alert(error);
        }
    })
});

$(document).on("submit", "#tambah_jadwal", function (e) {
    e.preventDefault();
    $.ajax({
        url: "/operasi/add/",
        method: "POST",
        data: {
            pasien: $("#pasien").find(":selected").val(),
            tanggal: $("#tanggal").val(),
            jam: $("#jam").val(),
            keterangan: $("#keterangan").val(),
            csrfmiddlewaretoken: "{{ csrf_token }}"
        },
        contentType: 'application/json; charset = utf-8',
        success: function(){
          alert('Jadwal operasi berhasil ditambahkan!');
          window.location.href = "/operasi/";
        },
        error: function(){
          alert("Gagal menambahkan jadwal operasi!");
        } 
      });
});