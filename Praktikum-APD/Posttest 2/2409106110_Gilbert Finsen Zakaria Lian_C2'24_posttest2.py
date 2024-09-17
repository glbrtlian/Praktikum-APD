nama= input("masukan nama: ")
nim= input("masukan NIM: ")
harga_setiap_mobil=int(input("masukan harga setiap mobil: "))

tesla_diskon = 0.17
toyota_diskon = 0.21
hyundai_diskon = 0.23

harga_setelah_diskon_tesla= harga_setiap_mobil - (harga_setiap_mobil * tesla_diskon)
harga_setelah_diskon_toyota= harga_setiap_mobil - (harga_setiap_mobil * toyota_diskon)
harga_setelah_diskon_hyundai= harga_setiap_mobil - (harga_setiap_mobil * hyundai_diskon)

harga_modulus = 7
#variable

print(f"mobil tesla seharga {harga_setiap_mobil} diskon 17% menjadi {harga_setelah_diskon_tesla:.2f},"
      f"mobil toyota seharga {harga_setiap_mobil} diskon 21% menjadi {harga_setelah_diskon_toyota:.2f},"
        f"mobil hyundai seharga {harga_setiap_mobil} diskon 23% menjadi {harga_setelah_diskon_hyundai:.2f},"
        f"dan harga_setiap_mobil modulus 7 adalah {harga_modulus:.2f}.")

