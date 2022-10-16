# My ToDo List
[Deployment Link for Assignment 5](http://tugas2yudi.herokuapp.com/todolist/)
* You have to create an account first!

# Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Internal CSS : adalah kode yang dituliskan di dalam file html kita sendiri dengan tag `<style>` pada bagian header. Penulisan CSS dalam tag tersebut sama seperti penulisan file.css yang dibuat sebagaimana external css. Pada external css, kita perlu mengimport filenya dengan melakukan `<link rel="stylesheet" href="tugas.css"/>` yang biasanya diletakan di tag `<head>`. Selain itu, ada pula inline css yang berarti kita perlu mendefine css yang digunakan dalam tiap elemen yang kita buat di file html kita, contohnya `<h2 style="color:blue; font-family: arial;">semoga lulus</h2>`

### Kelebihan Kekurangan
* Inline : bisa untuk tracing karena hanya menerapkan pada satu, gampang diperbaiki, lebih ringan karena load accessnya sebentar, akan tetapi cape karena hanya untuk apply ke 1 elemen.
* Internal : Bisa untuk set 1 halaman penuh, gaperlu import import, tapi kurang efisien kalo html kita banyak.
* External : loading website cepat, ukuran file makin kecil, bisa digunakan untuk beberapa file sekaligus, tapi kalo file css gagal load, halaman jadi ancur :D, kurang efektif kalo cuma buat diterapin sedikit.

# Jelaskan tag HTML5 yang kamu ketahui.
ada banyak tag yang ada di html 5 :D
contohnya ada `<h1>` hingga `<h6>` yang biasa kita pakai untuk header, ada `<p>` untuk tulis teks, terus ada `<form>` seperti lab sebelumnya untuk membuat form yang akan disubmit, kemudian ada `<img>` untuk import picture dan yang paling common `<div>` sebagai wadah atau tatakan untuk elemen yang akan dibuat di dalamnya. Selain itu ada `<ul>` `<li>` untuk membuat list, `<title>` untuk judul halaman. Dan lain - lain :D

# Jelaskan tipe-tipe CSS selector yang kamu ketahui.
" . " untuk selector class dari sebuah komponen,  " # " untuk select id yang kita tambahkan di sebuah komponen,  > atau child selector untuk memilih semua element yang ada di dalam atau child sebuah komponen. Selain itu, hal yang paling basic adalah element selector untuk memilih elemen yang kita gunakan contohnya h1, h2, h3, dan lain-lain.

# Checklist Box
### INSTALL TAILWIND
1. Install node.js
2. Menjalankan `python -m pip install django-tailwind`
3. Menambahkan tailwinds di installed_app settings.py
4. Membuat sebuah project untuk tailwindnya `python manage.py tailwind init` -> default theme
5. Tambahkan theme ke installed apps
6. Menambahkan `TAILWIND_APP_NAME = 'theme'` dan `INTERNAL_IPS = ["127.0.0.1",]` pada settings.py
7. Menginstall tailwind `python manage.py tailwind install`
8. Menambahkan tag `{% load tailwind_tags %}` dan `{% tailwind_css %}` pada file html yang ada di todolist/templates
9. Menambahkan `'django_browser_reload'` ke installed_apps di settings.py
10. Menambahkan ` "django_browser_reload.middleware.BrowserReloadMiddleware",` pada variable middleware di settings.py
11. Menambahkan `path("__reload__/", include("django_browser_reload.urls")),` pada urls.py di project_django
12. Menambahkan django-tailwind di pada requirements.txt
 
Setelah kita menambahkan tailwind, saya mengubah tampilan pada add.html, login.html, register.html, todolist.html menggunakan metode "mirip" inline. Membuat komponen berada di tengah pada tampilan login, register, dan create task dengan menggunakan `flex items-center justify-center`. Selain itu membuatnya menjadi bulat `rounded` agar tampilannya menarik, serta kustomisasi bentuk tombol yang ada. Untuk todolist.html, membuat sebuah div sebagai navbar untuk menampilan user, button add dan logout yang saya posisikan absolute agar berada di kanan. Pada bagian body, saya menggunakan card-views dengan grid grid-cols yang dipadukan dengan responsive tergantung size layar dengan sm: untuk small, lg: untuk large, dan md:medium yang sudah ditentukan oleh tailwind. Ketika sizenya lg, kita set agar 4 coloms `grid-cols-4`, tetapi untuk md atau layar tablet adalah `grid-cols-2` dan untuk smartphone `grid-cols-1`.
