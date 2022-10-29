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
        
      },
        error: function () {
        alert("Data gagal ditambahkan")
        window.location.href = "/pelayananKonseling/";
      },
    });
  });

  $(document).ready(function () {
    
    let tab = '';
      $.ajax({
        url: "/pelayananKonseling/show_json_konseling",
        type: "GET",
        dataType: "json",
        success: function(resp){
        $('#logPelayananKonseling').empty();
          let counter = 0;
          for (let i of resp){
            counter += 1;
            let nama = i.fields.nama;
            let status_user = i.fields.status_user;
            let bentuk_konseling = i.fields.bentuk_konseling;
            let status_konseling = i.fields.status_konseling;
            let msg_status_konseling = status_konseling ? `<p class="bg-green-200 w-fit rounded-2xl p-1">Sudah Selesai</p>` : `<p class="bg-red-500 w-fit rounded-2xl p-1">Sedang diproses</p>`

              tab += `
              <div class="" id="${i.pk}div">
                            <div id="${i.pk}" class="bg-white rounded-2xl p-8 flex w-fit flex-col gap-2 hover:drop-shadow-2xl transition duration-300 ease-in-out">
                                <p class="text-center text-xl font-semibold">${counter}</p>
                                <h3 class="text-center text-xl">${nama}</h3>
                                <div class="flex m-2 p-2 justify-center">
                                    <div>
                                        <div class="transition-opacity bg-gray-600 bg-opacity-10 rounded-2xl p-2">
                                        <p class="break-all">${status_user}</p>
                                        </div>
                                    </div>
                                </div>
                                <div>
                                  <p>Bentuk Konseling : ${bentuk_konseling} </p>
                                  <p>Status Konseling : ${msg_status_konseling}</p>
                                </div>
                            </div>
                        </div>
                        `;
          };
          $('#logPelayananKonseling').append(tab);
          document.getElementsByClassName("form-konseling").reset();
        }
      })
  });