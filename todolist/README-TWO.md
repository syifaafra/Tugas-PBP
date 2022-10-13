# Tugas 5
## Perbedaan antara _asynchronous programming_ dengan _synchronous programming_
Synchronous adalah proses jalannya program secara sequential, disini yang dimaksud sequential ada berdasarkan antrian ekseskusi program. Sedangkan Asynchronous adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Asynchronouse hampir disemua Bahasa pemrograman ada namun untuk PHP masih belum ada. PHP sebagai server side hanya menyediakan synchronous namun bisanya di WEB Developers tetap digunakan namun menggunakan AJAX (Asynchronous Javascript And XML) untuk proses Asynchronouse.

## Paradigma _Event-Driven Programming_
_Event-Driven Programming_ adalah pendekatan untuk membuat program dapat merespon sebuah/beberapa events. _Events_ dapat di-_trigger_ oleh pengguna, seperti dengan mengklik ikon atau memasukkan beberapa teks. Dalam sistem otomatis, sensor dapat digunakan untuk mendeteksi _events_ seperti ketika suhu tertentu tercapai di rumah kaca atau ketinggian air tertentu terdeteksi pada sistem pertahanan banjir.

Subrutin yang merespon _event_ disebut _event handler_. Penangan acara akan memastikan bahwa pemrosesan yang sesuai terjadi sebagai respons terhadap peristiwa yang memicunya.
## Penerapan _asynchronous programming_ pada AJAX
AJAX merupakan singkatan dari Asynchronous JavaScript And XML. AJAX menggunakan browser untuk meminta data dari web server dan JavaScript serta HTML DOM untuk menampilkan data. AJAX dapat menggunakan XML untuk mengirim data tetapi dapat juga menggunakan teks ataupun JSON. AJAX membuat halaman web memperbarui data secara asinkronus dengan mengirimkan data ke server di balik layar, artinya kita dapat memperbarui sebagian elemen data pada halaman tanpa harus me-reload keseluruhan halaman.  
Salah satu contoh penerapannya pada tugas 6 : Pada halaman `todolist` apabila user menekan tombol `Add (with AJAX)` maka masih pada halaman tersebut akan muncul form untuk membuat task baru, dan ketika di submit halaman tersebut otomatis akan di-refresh sehingga menampilkan task baru.

## Cara Implementasi
1. Membuat view  `show_todolist_json` untuk mendapatkan data json
2. Membuat view `add_task` yang akan mengimplementasikan AJAX
3. Memasukkan path `json/` dan `add_task` ke dalam `urls.y` di todolist

## Referensi :
* https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-5
* https://community.algostudio.net/memahami-synchronous-dan-asynchronous-dalam-pemrograman/

