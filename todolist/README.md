# Tugas 4

Link heroku : https://tugas-2-pbp-afra.herokuapp.com/todolist
![image](dummy1.png)
![image](dummy2.png)

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>? ##
`csrf_token` adalah nilai unik, rahasia, dan tidak terprediksi yang dihasilkan oleh aplikasi sisi server dan dikirimkan ke klien sedemikian rupa sehingga disertakan dalam permintaan HTTP berikutnya yang dibuat oleh klien. Saat permintaan selanjutnya dibuat, aplikasi sisi server memvalidasi bahwa permintaan tersebut menyertakan token yang diharapkan dan menolak permintaan jika token tidak ada atau tidak valid. `csrf_token`dapat mencegah serangan CSRF dengan membuat penyerang tidak mungkin membuat permintaan HTTP yang sepenuhnya valid yang cocok untuk diumpankan ke pengguna korban. Karena penyerang tidak dapat menentukan atau memprediksi nilai `csrf_token` pengguna, mereka tidak dapat membuat permintaan dengan semua parameter yang diperlukan aplikasi untuk memenuhi permintaan tersebut.

## Cara membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})?  ##
Kita tidak wajib menggunakan `{{ form.as_table }}` untuk membuat form. Form juga dapat dibuat secara manual dengan membuat tag <input> yang berisi atribut <name> ,<type>  dan <value> yang sesuai.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML. ##
Melalui request POST input dari user pada form akan dikirim ke server. Lalu dengan menggunakan function `create_task` pada `views.py` input tersebut diubah menjadi `Task` berupa class `CreateTask` di `forms.py`, 
kemudian menyimpan data menggunakan method `save`. Data yang sudah disimpan dapat diakses melalui `Task.objects.all()` di dalam `views.py` lalu dimasukkan ke context kemudian di-render sehingga dapat dipakai pada `templates` html.
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. ##
1. Membuat aplikasi `todolist` :
Menggunakan command `python manage.py startapp todolist`
2. Membuat model Task :
Pada `models.py` saya menambahkan class baru bernama `Task` dengan atribut berupa id, user, date, title, description dan fungsi untuk mengubah dirinya sendiri ke bentuk string dengan return berupa title-nya.
3. Implementasi form registrasi, login, dan logout
    * Registrasi : Saya membuat fungsi `register` pada `views.py` kemudian menggunakan `UserCreationForm` untuk membuat form registrasi. Jika input nya sudah valid, maka form tersebut akan di save kemudian kembali ke halaman login, jika tidak maka page register akan di-refresh kembali
    * Login : Saya membuat fungsi `login_user` pada `views.py` kemudian mendapatkan username dan password menggunakan `request.POST.get` lalu di autentikasi apakah user tersebut sudah terdaftar atau belum. Jika sudah, maka akan dipanggil fungsi `login` dengan parameter `request` lalu menuju page utama `todolist`. Jika tidak maka page login akan di-refresh kembali.
    * Logout : Saya membuat fungsi `logout_user` pada `views.py` yang berisi pemanggilan fungsi `logout` denga parameter `request` lalu kembali ke halaman login
4.  Membuat halaman utama todolist :
Halaman utama saya buat di `todolist.html`. Penjelasan code sudah terdapat di dokumentasi code.
5. Membuat halaman form untuk pembuatan task :
Halaman form saya buat di `create_task.html`. Penjelasan code sudah terdapat di dokumentasi code.
6. Membuat routing :
Pada `settings.py` dalam `project_django` saya menambahkan aplikasi `todolist` pada `INSTALLED_APPS`. Kemudian di `urlspatterns` milik `urls.py` dalam `project_django` saya menambahkan `path('todolist/', include('todolist.urls'))`. Terakhir, saya mengisi `urls.py` di folder `todolist` dengan code sebagai berikut.
7. Deployment ke Heroku :
Saat tugas 2, saya sudah melakukan Deployment ke Heroku, sehingga untuk Tugas 4, saya hanya perlu mengupdate repositori Github saya yang sudah tersambung ke Heroku.
8. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.

## Referensi ##
https://portswigger.net/web-security/csrf/tokens

