# Data mahasiswa disimpan dalam dictionary
data_mahasiswa = {}

# Fungsi untuk menambah data mahasiswa
def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    data_mahasiswa[nama] = {"tugas": tugas, "uts": uts, "uas": uas}
    print(f"Data mahasiswa {nama} telah ditambahkan.")

# Fungsi untuk menampilkan data mahasiswa
def tampilkan():
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa.")
    else:
        print("\nDaftar Nilai Mahasiswa:")
        for nama, nilai in data_mahasiswa.items():
            print(f"Nama: {nama}")
            print(f"  Nilai Tugas: {nilai['tugas']}")
            print(f"  Nilai UTS: {nilai['uts']}")
            print(f"  Nilai UAS: {nilai['uas']}")
            print("-" * 30)

# Fungsi untuk menghapus data mahasiswa berdasarkan nama
def hapus(nama):
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data mahasiswa {nama} telah dihapus.")
    else:
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

# Fungsi untuk mengubah data mahasiswa berdasarkan nama
def ubah(nama):
    if nama in data_mahasiswa:
        print(f"Edit data untuk {nama}:")
        tugas = float(input("Masukkan nilai tugas baru: "))
        uts = float(input("Masukkan nilai UTS baru: "))
        uas = float(input("Masukkan nilai UAS baru: "))
        data_mahasiswa[nama] = {"tugas": tugas, "uts": uts, "uas": uas}
        print(f"Data mahasiswa {nama} telah diubah.")
    else:
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

# Program utama
def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Hapus Data Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4/5): ")

        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            ubah(nama)
        elif pilihan == "5":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Menjalankan program
menu()
