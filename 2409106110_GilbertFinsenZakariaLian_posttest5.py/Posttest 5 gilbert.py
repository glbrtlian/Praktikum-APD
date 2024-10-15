users = [
    ("admin", "gilbert"),  
    ("user", "user")
]

JADWAL = []

def find_user(username, password):
    for user in users:
        if user[0] == username and user[1] == password:
            return True
    return False

while True:
    print("Pilih opsi:")
    print("1. Register") 
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == '1': 
        username = input("Buat username: ")
        password = input("Buat password: ")
        if any(user[0] == username for user in users):
            print("Username sudah terpakai, coba yang lain!")
        else:
            users.append((username, password))  
            print(f"Pengguna {username} berhasil didaftarkan!")

    elif pilihan == '2': 
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if find_user(username, password):
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
                    pilih = input("PILIH : ")
                    if pilih == "1":
                        HARI = input("hari : ")
                        tanggal = input("tanggal : ")
                        tempat = input("tempat : ")
                        PJ = input("penanggung jawab: ")
                        JADWAL.append((HARI, tanggal, tempat, PJ))  
                        print("Jadwal berhasil ditambahkan!")

                    elif pilih == "2":
                        if len(JADWAL) == 0:
                            print("Jadwal masih kosong.")
                        else:
                            for jadwal in JADWAL:
                                print(f"\nHARI: {jadwal[0]}\nTANGGAL: {jadwal[1]}\nTEMPAT: {jadwal[2]}\nPenanggung Jawab: {jadwal[3]}")

                    elif pilih == "3":
                        HARI_lama = input("HARI yang akan diubah: ")
                        found = False
                        for i, jadwal in enumerate(JADWAL):
                            if jadwal[0] == HARI_lama:
                                HARI_baru = input("hari baru: ")
                                tanggal_baru = input("tanggal baru: ")
                                tempat_baru = input("tempat baru: ")
                                PJ_baru = input("Penanggung jawab baru: ")
                                JADWAL[i] = (HARI_baru, tanggal_baru, tempat_baru, PJ_baru)  
                                found = True
                                print(f"Jadwal {HARI_lama} berhasil diubah.")
                                break
                        if not found:
                            print("Jadwal tidak ditemukan.")
                    
                    elif pilih == "4":
                        HARI_lama = input("HARI yang ingin dihapus: ")
                        for i, jadwal in enumerate(JADWAL):
                            if jadwal[0] == HARI_lama:
                                del JADWAL[i]
                                print(f"Jadwal {HARI_lama} berhasil dihapus.")
                                break
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
                    pilih = input("PILIH : ")
                    if pilih == "1":
                        HARI = input("hari : ")
                        tanggal = input("tanggal : ")
                        tempat = input("tempat : ")
                        PJ = input("penanggung jawab: ")
                        JADWAL.append((HARI, tanggal, tempat, PJ))  
                        print("Jadwal berhasil ditambahkan!")

                    elif pilih == "2":
                        if len(JADWAL) == 0:
                            print("Jadwal masih kosong.")
                        else:
                            for jadwal in JADWAL:
                                print(f"\nHARI: {jadwal[0]}\nTANGGAL: {jadwal[1]}\nTEMPAT: {jadwal[2]}\nPenanggung Jawab: {jadwal[3]}")

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
