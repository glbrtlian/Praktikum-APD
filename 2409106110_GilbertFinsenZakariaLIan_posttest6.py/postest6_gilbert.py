users = {
    "admin": {"password": "gilbert"},
    "user": {"password": "user"},
}  

JADWAL = {}

while True:
    print("Pilih opsi:")
    print("1. Register") 
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == '1': 
        username = input("Buat username: ")
        password = input("Buat password: ")
        if username in users:
            print("coba yang lain!")
        else:
            users[username] = {"password": password}
            print(f"Pengguna {username} berhasil didaftarkan!")

    elif pilihan == '2': 
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in users and users[username]["password"] == password:
            print(f"Login berhasil! Selamat datang, {username}")
            
            if username == "admin": 
                print(
                    """
                    ==============================
                    |        JADWAL RAPAT         |
                    ==============================
                    |    1. TAMBAH DATA           |
                    |    2. TAMPILKAN DATA        |
                    |    3. UBAH DATA             |
                    |    4. HAPUS DATA            |
                    |    5. KELUAR                |
                    ==============================
                    """
                )
                while True:
                    pilih = (input("PILIH : "))
                    if pilih == "1":
                        HARI= input("hari : ")
                        tanggal = input("tanggal : ")
                        tempat = input("tempat : ")
                        PJ= input("penanggung jawab: ")
                        JADWAL[HARI] = {
                            "tanggal": tanggal, 
                            "tempat": tempat, 
                            "penanggung jawab": PJ
                        }

                    elif pilih == "2":
                        if len(JADWAL) == 0:
                            print("jadwal masih kosong.")
                        else:
                            for hari, info in JADWAL.items():
                                print(f"\nHARI: {hari}\nTANGGAL: {info['tanggal']}\nTEMPAT: {info['tempat']}\nPenanggung Jawab: {info['penanggung jawab']}")

                    elif pilih == "3":
                        JADWAL_lama = input("HARI yang akan diubah: ")
                        if JADWAL_lama in JADWAL:
                            HARI_baru = input("hari baru: ")
                            tanggal_baru = input("tanggal baru: ")
                            tempat_baru = input("tempat baru: ")
                            PJ_baru = input("Penanggung jawab baru: ")
                            JADWAL[HARI_baru] = {
                                "tanggal": tanggal_baru, 
                                "tempat": tempat_baru, 
                                "penanggung jawab": PJ_baru
                            }
                            if HARI_baru != JADWAL_lama:
                                del JADWAL[JADWAL_lama]
                            print(f"Jadwal {JADWAL_lama} berhasil diubah.")
                        else:
                            print("jadwal tidak ditemukan.")
                    
                    elif pilih == "4":
                        JADWAL_lama = input("Jadwal rapat yang ingin dihapus: ")
                        if JADWAL_lama in JADWAL:
                            del JADWAL[JADWAL_lama]
                            print(f"jadwal {JADWAL_lama} berhasil dihapus.")
                        else:
                            print("Jadwal tidak ditemukan.")
                    
                    elif pilih == "5":
                        print("Terima kasih, kembali ke menu login.")
                        break
                    
                    else:
                        print("Pilihan tidak valid!")
            
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
                while True:
                    pilih = (input("PILIH : "))
                    if pilih == "1":
                        HARI = input("hari : ")
                        tanggal = input("tanggal : ")
                        tempat = input("tempat : ")
                        PJ = input("penanggung jawab: ")
                        JADWAL[HARI] = {
                            "tanggal": tanggal, 
                            "tempat": tempat, 
                            "penanggung jawab": PJ  
                        }

                    elif pilih == "2":
                        if len(JADWAL) == 0:
                            print("jadwal masih kosong.")
                        else:
                            for hari, info in JADWAL.items():
                                print(f"\nHARI: {hari}\nTANGGAL: {info['tanggal']}\nTEMPAT: {info['tempat']}\nPenanggung Jawab: {info['penanggung jawab']}")

                    elif pilih == "3":  
                        print("Terima kasih, kembali ke menu login.")
                        break
                    
                    else:
                        print("Pilihan tidak valid!")

        else:
            print("Login gagal! Username atau password salah.")
    
    elif pilihan == '3': 
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid, coba lagi!")