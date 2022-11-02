$(document).ready(function () {
  let tab = '';
    $.ajax({
      url: "/pelayananDokter/show_log",
      type: "GET",
      dataType: "json",
      success: function(resp){
        let counter = 0;
        for (let i of resp){
          counter += 1;
            tab += `
            <div class="" id="${i.pk}div">
                          <div id="${i.pk}" class="bg-white rounded-2xl p-8 flex w-fit flex-col gap-2 hover:drop-shadow-2xl transition duration-300 ease-in-out">
                              <div>
                                <p>Bulan : ${i.fields.bulan} </p>
                                <p>Keterangan : ${i.fields.keterangan}</p>
                              </div>
                          </div>
                      </div>
                      `;
        };
        $('#logPesanan').append(tab);
      }
    })
});

  $(document).on("submit", "#tembak_db", function (e) {
    e.preventDefault();
    console.log("mau masuk ajax");
    $.ajax({
      type: "POST",
      url: "/pembayaran/keterangan/add/",
      data: {
        bulan: $("#id_bulan").val(),
        keterangan: $("#id_keterangan").val(),
        csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val(),
      },
      dataType: "json",
      success: function () {
        alert("Data berhasil ditambahkan ke file JSON")
        window.location.replace(" ")
      },
    });
  });