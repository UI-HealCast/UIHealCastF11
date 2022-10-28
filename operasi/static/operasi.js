$(document).ready(function () {
    $.ajax({
        url: "/operasi/json/",
        method: "GET",
        dataType: "json",
        success: function(data){
          var table = $('#tableJadwal');
          table.empty();
          if (data == '') {
            table.append("<div class='flex justify-center bg-yellow-300 p-3 rounded-2xl'>" +
            "<p>Tidak ada jadwal operasi!</p></div>");
          } else {
            table.append(`<div class='overflow-x-auto relative shadow-md sm:rounded-lg'>
                            <table class='w-full text-sm text-left text-gray-500 dark:text-gray-400'>
                              <thead class='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'>
                                  <tr>
                                    <th scope='col' class='py-3 px-6'>
                                          Dokter
                                      </th>
                                      <th scope="col" class="py-3 px-6">
                                          Pasien
                                      </th>
                                      <th scope="col" class="py-3 px-6">
                                          Tanggal
                                      </th>
                                      <th scope="col" class="py-3 px-6">
                                          Jam
                                      </th>
                                      <th scope="col" class="py-3 px-6">
                                          Keterangan
                                      </th>
                                      <th scope="col" class="py-3 px-6">
                                          Hapus
                                      </th>
                                  </tr>
                              </thead>
                              <tbody>`);
            $(data).each(function(key, val){
              table.append(`<tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                              <td class="py-4 px-6">
                                  ${val.fields.usernameDokter}
                              </td>
                              <td class="py-4 px-6">
                                  ${val.fields.usernamePasien}
                              </td>
                              <td class="py-4 px-6">
                                  ${val.fields.tanggal}
                              </td>
                              <td class="py-4 px-6">
                                  ${val.fields.jam}
                              </td>
                              <td class="py-4 px-6">
                                  ${val.fields.keterangan}
                              </td>
                              <td class="flex items-center py-4 px-6 space-x-3">
                                  <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">Remove</a>
                              </td>
                            </tr>`);
            });
            
            table.append(`</tbody>
                        </table>
                      </div>`);
          }
        },
        error: function(error){
          alert(error);
        }
    })
});

$(document).on("submit", "#tambah_jadwal", function (e) {
    e.preventDefault();
    var token = $("#tambah_jadwal").find('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
        url: "/operasi/add/",
        method: "POST",
        data: {
            pasien: $("#id_pasien option:selected").text(),
            tanggal: $("#id_tanggal").val(),
            jam: $("#id_jam").val(),
            keterangan: $("#id_keterangan").val(),
            csrfmiddlewaretoken: token
        },
        dataType: "json",
        success: function(){
          alert('Jadwal operasi berhasil ditambahkan!');
          window.location.href = "/operasi/";
        },
        error: function(){
          alert("Gagal menambahkan jadwal operasi!");
        } 
      });
});