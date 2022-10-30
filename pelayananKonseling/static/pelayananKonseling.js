
  function handleCard(){
    $("#logPelayananKonseling").empty();
    $(".form-konseling").trigger("reset");

    var isDokter = document.getElementById("isDokter").value;
    var isPasien = document.getElementById("isPasien").value;

    if (isDokter == "True"){
        var URL = "/pelayananKonseling/show_json_konseling_dokter" 
    }
    else {
        var URL = "/pelayananKonseling/show_json_konseling"
    }

    $.ajax({
        type: "GET",
        url: URL,
        dataType: "json",
        success: function (resp) {
            let counter = 0;
            for (let i of resp){
                counter += 1;
                let nama = i.fields.nama;
                let status_user = i.fields.status_user;
                let bentuk_konseling = i.fields.bentuk_konseling;
                let status_konseling = i.fields.status_konseling;

                let msg_hari_senin = i.fields.senin ? "Senin" : "";
                let msg_hari_selasa = i.fields.selasa ? "Selasa" : "";
                let msg_hari_rabu = i.fields.rabu ? "Rabu" : "";
                let msg_hari_kamis = i.fields.kamis ? "Kamis" : "";
                let msg_hari_jumat = i.fields.jumat ? "Jumat" : "";
                let msg_hari_sabtu = i.fields.sabtu ? "Sabtu" : "";
                let msg_hari_minggu = i.fields.minggu ? "Minggu" : "";

                let msg_waktu_pagi = i.fields.pagi ? "Pagi" : "";
                let msg_waktu_siang = i.fields.siang ? "Siang" : "";
                let msg_waktu_sore = i.fields.sore ? "Sore" : "";
              let msg_waktu_malam = i.fields.malam ? "Malam" : "";
              
              let button=''
              if (isDokter == "True") {
                button = `
                <a class="inline-flex items-center h-8 px-4 m-2 text-sm transition-colors duration-150 border-solid border-2 border-black rounded-lg focus:shadow-outline hover:bg-black hover:text-white"
                href="set-konseling/${i.pk}">Ubah Status</a>
                `
              } else {
                button = ""
              }
                

                let msg_status_konseling = status_konseling ? `<p class="bg-green-200 w-fit rounded-2xl p-1">Sudah Selesai</p>` : `<p class="bg-red-500 w-fit rounded-2xl p-1">Sedang diproses</p>`

                let tab = `
                <div class="" id="${i.pk}div">
                              <div id="${i.pk}" class="bg-white rounded-2xl p-8 flex w-fit flex-col gap-2 hover:drop-shadow-2xl transition duration-300 ease-in-out">
                                  <p class="text-center text-2xl font-semibold">${counter}</p>
                                  <h3 class="text-center text-2xl">${nama}</h3>
                                  <div class="flex m-2 p-2 justify-center">
                                      <div>
                                          <div class="transition-opacity bg-gray-600 bg-opacity-10 rounded-2xl p-2">
                                          <p class="break-all">${status_user}</p>
                                          </div>
                                      </div>
                                  </div>
                                  <div>
                                    <p><b>Bentuk Konseling</b> : ${bentuk_konseling} </p>
                                    <p><b>Status Konseling</b> : ${msg_status_konseling}</p>
                                    <p><b>Hari</b> : ${msg_hari_senin} ${msg_hari_selasa} ${msg_hari_rabu} ${msg_hari_kamis} ${msg_hari_jumat} ${msg_hari_sabtu} ${msg_hari_minggu}</p>
                                    <p><b>Waktu</b> : ${msg_waktu_pagi} ${msg_waktu_siang} ${msg_waktu_sore} ${msg_waktu_malam}</p>
                                  </div>
                                  <div class="flex justify-center">
                                    ${button}
                                  </div>
                              </div>
                          </div>
                          `;
                $("#logPelayananKonseling").append(tab);
            }
        },
    });
  }

  function createPelayananKonseling() {
    // validate form
    var form = document.getElementsByClassName("form-konseling")[0];
    if (form.checkValidity() === false) {
        return false;
    }


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
        success: function () {
          handleCard();
        }
        });
  }

  $(document).ready(function () {
    handleCard();
})