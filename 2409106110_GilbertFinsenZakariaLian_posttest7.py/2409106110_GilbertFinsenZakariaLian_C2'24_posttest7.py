# Variabel global
users = {
    "admin": {"password": "gilbert"},
    "user": {"password": "user"},
}  

JADWAL = {}

# Fungsi untuk menambahkan jadwal
def tambah_jadwal(hari, tanggal, tempat, pj):
    global JADWAL
    JADWAL[hari] = {"tanggal": tanggal, "tempat": tempat, "penanggung jawab": pj}
    print(f"Jadwal pada hari {hari} berhasil ditambahkan.")


# Fungsi untuk menghitung total jadwal
def hitung_total_jadwal():
    return len(JADWAL)

# Prosedur untuk login
def proses_login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in users and users[username]["password"] == password:
        print(f"Login berhasil! Selamat datang, {username}")
        return username
    else:
        print("Login gagal! Username atau password salah.")
        return None

# Prosedur untuk menampilkan menu utama
def tampilkan_menu(role):
    if role == "admin":
        print(
            """
            ==============================
            |        JADWAL RAPAT         |
            ==============================
            |    1. TAMBAH DATA           |
            |    2. TAMPILKAN DATA        |
            |    3. UBAH DATA             |
            |    4. HAPUS DATA            |
            |    5. HITUNG TOTAL JADWAL   |
            |    6. KELUAR                |
            ==============================
            """
        )
    else:
        print(
            """
            ==============================
            |       JADWAL RAPAT          |
            ==============================
            |    1. TAMBAH DATA           |
            |    2. TAMPILKAN DATA        |
            |    3. KELUAR                |
            ==============================
            """
        )

# Program utama
while True:
    print("\nPilih opsi:")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == '1': 
        username = input("Buat username: ")
        password = input("Buat password: ")
        if username in users:
            print("Username sudah digunakan, coba yang lain!")
        else:
            users[username] = {"password": password}
            print(f"Pengguna {username} berhasil didaftarkan!")

    elif pilihan == '2': 
        username = proses_login()

        if username:
            if username == "admin":
                while True:
                    tampilkan_menu("admin")
                    pilih = input("PILIH: ")

                    if pilih == "1":
                        hari = input("Hari: ")
                        tanggal = input("Tanggal: ")
                        tempat = input("Tempat: ")
                        pj = input("Penanggung Jawab: ")
                        tambah_jadwal(hari, tanggal, tempat, pj)

                    elif pilih == "2":
                        if len(JADWAL) == 0:
                            print("Jadwal masih kosong.")
                        else:
                            for hari, info in JADWAL.items():
                                print(f"\nHARI: {hari}\nTANGGAL: {info['tanggal']}\nTEMPAT: {info['tempat']}\nPenanggung Jawab: {info['penanggung jawab']}")

                    elif pilih == "3":
                        hari_lama = input("Hari yang akan diubah: ")
                        if hari_lama in JADWAL:
                            hari_baru = input("Hari baru: ")
                            tanggal_baru = input("Tanggal baru: ")
                            tempat_baru = input("Tempat baru: ")
                            pj_baru = input("Penanggung Jawab baru: ")
                            JADWAL[hari_baru] = {"tanggal": tanggal_baru, "tempat": tempat_baru, "penanggung jawab": pj_baru}
                            if hari_baru != hari_lama:
                                del JADWAL[hari_lama]
                            print(f"Jadwal {hari_lama} berhasil diubah.")
                        else:
                            print("Jadwal tidak ditemukan.")
                    
                    elif pilih == "4":
                        hari_hapus = input("Hari yang ingin dihapus: ")
                        if hari_hapus in JADWAL:
                            del JADWAL[hari_hapus]
                            print(f"Jadwal {hari_hapus} berhasil dihapus.")
                        else:
                            print("Jadwal tidak ditemukan.")

                    elif pilih == "5":
                        print(f"Total jadwal: {hitung_total_jadwal()}")

                    elif pilih == "6":
                        print("Terima kasih, kembali ke menu login.")
                        break

                    else:
                        print("Pilihan tidak valid!")

            else:
                while True:
                    tampilkan_menu("user")
                    pilih = input("PILIH: ")

                    if pilih == "1":
                        hari = input("Hari: ")
                        tanggal = input("Tanggal: ")
                        tempat = input("Tempat: ")
                        pj = input("Penanggung Jawab: ")
                        tambah_jadwal(hari, tanggal, tempat, pj)

                    elif pilih == "2":
                        if len(JADWAL) == 0:
                            print("Jadwal masih kosong.")
                        else:
                            for hari, info in JADWAL.items():
                                print(f"\nHARI: {hari}\nTANGGAL: {info['tanggal']}\nTEMPAT: {info['tempat']}\nPenanggung Jawab: {info['penanggung jawab']}")

                    elif pilih == "3":
                        print("Terima kasih, kembali ke menu login.")
                        break

                    else:
                        print("Pilihan tidak valid!")
    
    elif pilihan == '3': 
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid, coba lagi!")
