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
                    <div class="" id="${i.pk}div" onClick=showData(${i.pk})>
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
            console.log("Update berhasil");
            getDokter();
        }
    });
}