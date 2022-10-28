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
              let statusDokter = i.fields.status;
              let statusObat = i.fields.statusObat;
              mssgDokter = statusDokter ? `<p class="bg-green-200 w-fit rounded-2xl p-1">Selesai diperiksa</p>` : `<p class="bg-red-500 w-fit rounded-2xl p-1">Belum diperiksa</p>`
              mssgObat = statusObat ? `<p class="bg-green-200 w-fit rounded-2xl p-1">Obat dapat diambil</p>` : `<p class="bg-red-500 w-fit rounded-2xl p-1">Obat sedang diproses</p>`
              tab += `
              <div class="" id="${i.pk}div">
                            <div id="${i.pk}" class="bg-white rounded-2xl p-8 flex w-fit flex-col gap-2 hover:drop-shadow-2xl transition duration-300 ease-in-out">
                                <p class="text-center text-xl font-semibold">${counter}</p>
                                <p class="text-center text-xs">${i.fields.tanggal_janji.slice(0,10)} ${i.fields.tanggal_janji.slice(11,19)} </p>
                                <div class="flex m-2 p-2 justify-center">
                                    <div>
                                        <div class="transition-opacity bg-gray-600 bg-opacity-10 rounded-2xl p-2">
                                        <p class="break-all">${i.fields.dokter}</p>
                                        </div>
                                    </div>
                                </div>
                                <div>
                                  <p>Status Konsultasi : ${mssgDokter} </p>
                                  <p>Status Obat : ${mssgObat   }</p>
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
    $.ajax({
      type: "POST",
      url: "/pelayananDokter/add/",
      data: {
        dokter: $("#id_dokter").find(":selected").val(),
        keluhan: $("#id_keluhan").val(),
        noHP: $("#id_noHP").val(),
        csrfmiddlewaretoken: "{{ csrf_token }}",
      },
      dataType: "json",
      success: function () {
        alert("Data berhasil ditambahkan")
        window.location.href = "/pelayananDokter/";
      },
    });
  });