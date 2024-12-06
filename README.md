# Penjelasan Program
1. Fungsi tambah : Menambahkan data mahasiswa baru ke dalam dictionary.

    Mengambil input berupa nama mahasiswa, nilai tugas, nilai UTS, dan nilai UAS.
    Data tersebut disimpan dalam dictionary data_mahasiswa dengan nama sebagai key, dan nilai tugas, UTS, dan UAS sebagai value dalam bentuk dictionary.

3. Fungsi tampilkan : Menampilkan daftar data mahasiswa yang sudah ada.

    Jika tidak ada data mahasiswa, program akan menampilkan pesan "Tidak ada data mahasiswa".
    Jika ada data, program akan mencetak nama mahasiswa beserta nilai tugas, UTS, dan UAS.

4. Fungsi hapus(nama) : Menghapus data mahasiswa berdasarkan nama.
    Mengecek apakah nama mahasiswa ada dalam data_mahasiswa. Jika ada, data akan dihapus menggunakan del.
    Jika tidak ada, program akan memberi pesan bahwa mahasiswa tidak ditemukan.

5. Fungsi ubah(nama) : Mengubah data mahasiswa yang sudah ada.

    Mengecek apakah nama mahasiswa ada dalam data_mahasiswa. Jika ada, program akan meminta input baru untuk nilai tugas, UTS, dan UAS, lalu mengupdate data mahasiswa.
    Jika tidak ada, program akan memberi pesan bahwa mahasiswa tidak ditemukan.

6. Fungsi menu() : Menampilkan menu utama program dan menerima input dari pengguna untuk memilih aksi.

    Program akan terus berjalan dalam loop dan menampilkan menu sampai pengguna memilih untuk keluar dengan memilih opsi "5".
    Berdasarkan input pengguna, fungsi yang sesuai (tambah(), tampilkan(), hapus(), ubah()) akan dipanggil.

7. Program Utama
    Program utama menjalankan fungsi menu() yang berisi pilihan interaktif bagi pengguna untuk mengelola data mahasiswa.

# Alur Program
1.	Program dimulai dan menampilkan menu.
2.	Pengguna memilih salah satu opsi:

  	1 untuk menambah data mahasiswa.

  	2 untuk menampilkan data mahasiswa.

  	3 untuk menghapus data mahasiswa.

  	4 untuk mengubah data mahasiswa.

  	5 untuk keluar.
4.	Berdasarkan pilihan, program akan menjalankan fungsi yang sesuai dan kembali menampilkan menu setelah selesai.
5.	Program berakhir ketika pengguna memilih untuk keluar (pilihan 5).

