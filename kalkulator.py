
# PROGRAM KALKULATOR SEDERHANA

print("=== KALKULATOR SEDERHANA ===")
print("1. Tambah (+)")
print("2. Kurang (-)")
print("3. Kali (*)")
print("4. Bagi (/)")

pilihan = input("Pilih operasi (1/2/3/4): ")

if pilihan in ('1', '2', '3', '4'):

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        hasil = angka1 + angka2

    elif pilihan == '2':
        hasil = angka1 - angka2

    elif pilihan == '3':
        hasil = angka1 * angka2

    elif pilihan == '4':
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            hasil = "Tidak bisa membagi dengan nol!"

    print("Hasil:", hasil)

else:
    print("Pilihan tidak valid!")
