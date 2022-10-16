# My ToDo List
[Deployment Link for Assignment 4](http://tugas2yudi.herokuapp.com/todolist/)
* You have to create an account first!

# Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Kegunaan dari csrf token pada elemen form adalam untuk membandingan key csrf ketika sebuah end-user ingin melakukan method post atau get, form tersebut akan merespons OK jika form disubmit atau diakses dengan user_session yang tepat. 

Jika kita tidak menggunakan csrf token, website yang kita miliki tetap akan berjalan dengan baik, akan tetapi mungkin ada beberapa route link sensitif yang bisa diakses secara umum oleh orang (contoh logout atau delete account dengan mengakses /delete=id?1234123. Jika sembarang orang atau website lain punya button yang href ke link itu, akun kita otomatis bisa terhapus atau terlogout tanpa kita sadari.

# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Kita bisa saja membuat elemen form tanpa menggunakan form.as_table. Jika menggunakan itu, mungkin ada beberapa variable yang ada di database tidak memerlukan di-POST sehingga kita dapat membuat form manual untuk mengatasinya. Form manual dibuat dengan membuat <form> dengan method post dan tentunya diisi csrf token. Setelah itu, buat tag table yang berisikan <tr>, dan didalam tr tersebut kita berikan tag input dengan hal penting type menyesuaikan kebutuhan dan name untuk identifier. Setelah form disubmit, akan dikembalikan ke fungsi yang memanggil form tersebut dan kita dapat mengakses input yang dimasukkan dengan menggunakan method `request.POST.get(name yang kita buat di table tadi)`.

# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Setelah user menekan tombol submit, data data yang input bisa diakses dengan menggunakan method `request.POST.get(name while creating input)`. setelah mendapatkan data yang diinput, kita bisa melakukan create database dengan menggunakan `"Models".objects.create(name = data input)` dengan name sesuai yang sudah kita buat di `todolist/models.py`. Setelah itu, as usual, data tersebut tersimpan di database django yang perlu kita akses dengan (dalam konteks ini menggunakan filter karena harus sesuai dengan user) `"Models".objects.filter(user=request.user)` dan kita deliver kedalam context agar kita ikut render ke html. Setelah direturn render dengan target html. object yang sudah kita filter tadi bisa kita loop dengan for each (contoh : `{% for todo in list_todo %}` list_todo karena data obj yang disimpan disini berada pada variable list_todo). Selanjutnya, dalam loop, bisa kita tampilan data apa saja yang mau kita tampilkan dengan mengakses atributnya :D contoh `{{todo.status}}` dan lain-lain.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Menjalankan `python manage.py startapp todolist` di folder root.
2. Menambahkan `path('todolist/', include('todolist.urls')),` di urls.py. .project django agar route dengan url yang ada di todolist dan menjalankan fungsi show_todo yang ada di `todolist/views.py`.
3. Membuat class di `todolist/models.py` dan membuatnya field sesuai yang disuruh di tugas.
4. Membuat fungsi login, logout, register yang masing masing terhubung dengan login.html dan register.html dan membuat restriksi agar user harus login dahulu dengan menambahkan `@login_required(login_url='/todolist/login/')` diatas fungsi yang merupakan main dari project.
5. Mengedit bagian html agar menampikan user dengan mengakses variable yang ada di contexx (`{{username}}`) dan membuat dua buah button yang masing-masing memiliki logical command untuk logout, tambah task baru, dan membuat tabel untuk menampilkan data-data todolist yang sudah disubmit ke database.
6. Ketika user memencet tombol tambah task, user akan diarahkan ke halaman baru `todolist/create-task` dan akan membuat form yang berisi task dan description yang akan dikirim ke fungsi create di views.py untuk ditambahkan ke database.
7. Membuat route agar terhubung dengan fungsi fungsi yang ada di views py ketika mengakses link todolist/register, login, create-task, delete, change, dan lain-lain.
8. Deploy ke heroku dan membuat 2 user dengan masing-masing 3 dummy list to do.
