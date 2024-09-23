

# Input harga mobil
harga = float(input("Masukkan harga mobil: "))

# Input merek mobil
merek = input("Masukkan merek mobil (Tesla, Toyota, Hyundai): ")

# Kondisi untuk menentukan diskon
if merek == "Tesla":
    persen_diskon = 0.17
elif merek == "Toyota":
    persen_diskon = 0.21
elif merek == "Hyundai":
    persen_diskon = 0.23
else:
    print("Bu Navira tidak jadi membeli mobil.")
    exit()

# Menghitung diskon
diskon = harga * persen_diskon

# Menghitung harga setelah diskon
harga_setelah_diskon = harga - diskon

# Menampilkan hasil
print(f"Harga setelah diskon untuk {merek} adalah: {harga_setelah_diskon}")