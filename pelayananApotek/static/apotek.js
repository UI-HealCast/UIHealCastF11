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
            console.log(data);
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
});
