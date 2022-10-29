$(document).on("submit", "#tembak_dbKonseling", function (e) {
    e.preventDefault();
    $.ajax({
      type: "POST",
      url: "/pelayananKonseling/tembakDBAjax/",
      data: {
        nama: $("#id_nama").val(),
        status_user: $("#id_status_user").find(":selected").val(),
        email: $("#id_email").val(),
        bentuk_konseling: $("#id_bentuk_konseling").find(":selected").val(),
        keluhan_konseling: $("#id_keluhan_konseling").val(),
        senin: $("#id_senin").is(":checked"),
        selasa: $("#id_selasa").is(":checked"),
        rabu: $("#id_rabu").is(":checked"),
        kamis: $("#id_kamis").is(":checked"),
        jumat: $("#id_jumat").is(":checked"),
        sabtu: $("#id_sabtu").is(":checked"),
        minggu: $("#id_minggu").is(":checked"),
        pagi: $("#id_pagi").is(":checked"),
        siang: $("#id_siang").is(":checked"),
        sore: $("#id_sore").is(":checked"),
        malam: $("#id_malam").is(":checked"),
        noHP: $("#id_noHP").val(),
        csrfmiddlewaretoken: "{{ csrf_token }}",
      },
      dataType: "json",
      success: function () {
        alert("Data berhasil ditambahkan")
        window.location.href = "/pelayananKonseling/";
      },
        error: function () {
        alert("Data gagal ditambahkan")
        window.location.href = "/pelayananKonseling/";
      },
    });
  });

