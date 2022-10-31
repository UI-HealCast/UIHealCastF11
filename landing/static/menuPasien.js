const toggle = document.querySelector('.toggle input')

function loadData() {
    let tab= "";
    $.ajax({
        url: "/list-pasien/",
        type: "GET",
        dataType: "json",
        success: function(resp){  
            for (let i of resp){
                let status = i.fields.status;
                let type = i.pk;

                if (!status){
                    tab +=`
                    <a href="/menu-pasien/edit/${type}">
                    <div class="" id="${i.pk}div">
                        <div id="${i.pk}" class="bg-white rounded-2xl p-8 flex flex-col gap-2 hover:drop-shadow-2xl transition duration-300 ease-in-out">
                            <p class="text-center text-xl font-semibold">${i.fields.username}</p>
                            <p class="text-center text-xs">${i.fields.tanggal_janji.slice(0,10)} ${i.fields.tanggal_janji.slice(11,19)} </p>
                            <div class="flex m-2 p-2 flex-col">
                                <div class="transition-opacity bg-gray-600 bg-opacity-10 rounded-2xl p-2">
                                <p class="break-all">${i.fields.keluhan}</p>
                                </div>
                                <p class="break-all">${i.fields.noHP}</p>
                            </div>
                        </div>
                    </div>
                    </a>
                    `
                }
                
            ;
            $('#listPat').html(tab);
            }
        },
        error: function(resp){
            console.log('Error?');
        }
    })
};

$(document).ready(function () {
    loadData();
    getDokter();
});


function getDokter(){
    $.ajax({
        url: "/show-dokter/",
        type: "GET",
        dataType: "json",
        success: function(resp){
            let masuk = resp[0].fields.doctorReady
            const onOff = toggle.parentNode.querySelector('.onoff')
            onOff.textContent = masuk ? 'Tersedia' : 'Tidak Tersedia'
            document.querySelector('#checkedDokter').checked = masuk
        }
    })
}


function changeStatus(){
    $.ajax({
        url: "/change-status/",
        type: 'PATCH',
        success: function (data) {
            getDokter();
        }
    });
}

$(document).ready(function () {
    handleCard();
})
  
function handleCard(){
    $("#listKonseling").empty();

    $.ajax({
        type: "GET",
        url: '/show_json_konseling_dokter/',
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
              
              let button = `
                <a class="inline-flex items-center h-8 px-4 m-2 text-sm transition-colors duration-150 border-solid border-2 border-black rounded-lg focus:shadow-outline hover:bg-black hover:text-white"
                href="set-konseling/${i.pk}">Ubah Status</a>

                <a class="inline-flex items-center h-8 px-4 m-2 text-sm transition-colors duration-150 border-solid border-2 border-black rounded-lg focus:shadow-outline hover:bg-black hover:text-white"
                onclick="deleteRiwayat(${i.pk});">Hapus Riwayat</a>
                `     
                
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
                $("#listKonseling").append(tab);
            }
        },
    });
}
  
function deleteRiwayat(id) {
		$.ajax({
			url: `./delete/${id}`,
			dataType: "json",
			success: function () {
				$(`#${id}`).remove();
			}
		})
}