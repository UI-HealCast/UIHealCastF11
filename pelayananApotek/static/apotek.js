function show_data_obat() {
    $.ajax({
        url: "/pelayananApotek/json",
        type: "GET",
        dataType: "json",
        success: function(data){

        for (i of data){
            status = i.fields.status_obat ? "Tersedia" : "Tidak Tersedia";
            result = `
            <tr id="${i.pk}"><td>${i.fields.nama_obat}</td>
                <td>${i.fields.description}</td>
                <td>${i.fields.harga}</td>
                <td id="status-obat-${i.pk}">${status}
                    <button class="bg-green-500 hover:bg-green-700 rounded-2xl p-2 text-white font-bold delete" onclick="change_status_obat(${i.pk})">
                    Ubah</button>
                </td>
                <td><button class="bg-red-500 rounded-2xl hover:bg-red-700 p-2 text-white font-bold delete" onclick="delete_obat(${i.pk})">
                    Remove</button></td></tr>`

            $("#table-obat tbody").prepend(result);
        }   
        },
        error: function(data) {
            console.log('Error')
        }
    })
};
function delete_obat(pk){
    $.ajax({
        url: `/pelayananApotek/delete_obat/${pk}`,
        csrfmiddlewaretoken: "{{ csrf_token }}",
        type: "DELETE",
        success: function(data) {
            $(`#${pk}`).remove()
        }
    })
};
function change_status_obat(pk){
$.ajax({
    url: `/pelayananApotek/change_status_obat/${pk}`,
    success: function(data) {
        status = data === "True" ? "Tersedia" : "Tidak Tersedia";
        $("#status-obat-"+pk).replaceWith(`<td id="status-obat-${pk}">${status}
                    <button class="bg-green-500 rounded-2xl p-2 text-white font-bold delete" onclick="change_status_obat(${pk})">
                    Ubah</button>`);
    }
})
};

$(document).on("submit", "#form-add-obat", function (e){
    e.preventDefault();
    var data = {
        nama_obat: $("#id_nama_obat").val(),
        description: $("#id_description").val(),
        harga: $("#id_harga").val(),
        csrfmiddlewaretoken: "{{ csrf_token }}"
    };
    console.log(data); 
    $.ajax({
        type: "POST",
        url: "/pelayananApotek/add_obat/",
        data: data,
        dataType: "json",
        success: function (data) {
        
            status = data.fields.status_obat ? "Tersedia" : "Tidak Tersedia";
            result = `
            <tr id="${data.pk}"><td>${data.fields.nama_obat}</td>
                <td>${data.fields.description}</td>
                <td>${data.fields.harga}</td>
                <td id="status-obat-${data.pk}">${status}
                    <button class="bg-green-500 hover:bg-green-700 rounded-2xl p-2 text-white font-bold delete" onclick="change_status_obat(${data.pk})">
                            Ubah</button></td>
                <td><button class="bg-red-500 hover:bg-red-700 rounded-2xl p-2 text-white font-bold delete" onclick="delete_obat(${data.pk})">
                    Remove</button></td></tr>`
            $("#table-obat tbody").prepend(result);
            alert("Data berhasil ditambahkan")
            $("#form-add-obat").each(function(){
            this.reset();
        });
    },
    });
});

$(document).ready(function () {
    show_data_obat();
    show_status_pasien();
    
});

function show_status_pasien(){
    $.ajax({
        url: "/pelayananApotek/show_patient_json",
        type: "GET",
        dataType: "json",
        success: function(data){
            for (i of data){
                status = i.statusObat ? "Obat sudah bisa diambil" : "Obat belum bisa diambil";
                result = `
                <div class="w-60 p-2 bg-red-50 rounded-xl transform transition-all hover:-translate-y-2 duration-300 shadow-lg hover:shadow-2xl">
        
                <div class="p-2">
                    <h2 class="font-bold text-lg mb-2 ">${i.fields.username}</h2>
                    <!-- Description -->
                    <p class ="font-bold text-gray-800">Dokter yang menangani</p>
                    <p class="text-sm text-gray-800">${i.fields.usernameDokter}</p>
        
                    <p class ="font-bold text-gray-800">Status</p>
                    <p class="text-sm text-gray-800" id="status-pasien-${i.pk}">${status}</p>
        
                </div>
                <!-- CTA -->
                <div class="m-2">
                    <button onclick="change_status_pasien(${i.pk})" 
                            class = "text-white bg-blue-500 px-3 py-1 rounded-md hover:bg-blue-700">Change Status</button>
                </div>
                </div>`

                $("#daftar-pasien").append(result);
            }   
            },
            error: function(data) {
                console.log('Error')
            }
    })
};
function change_status_pasien(pk){
    $.ajax({
        url: `/pelayananApotek/change_status/${pk}`,
        success: function(data) {
            status = data === "True" ? "Obat sudah bisa diambil" : "Obat belum bisa diambil";
            $("#status-pasien-"+pk).replaceWith(`<p class="text-sm text-gray-800" id="status-pasien-${pk}">${status}</p>`);
        }
    })
};
