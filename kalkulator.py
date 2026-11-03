# Program Kalkulator Sederhana
print("=== KALKULATOR SEDERHANA ===")
print("1. Tambah (+)")
print("2. Kurang (-)")

pilihan = input("Pilih operasi (1/2): ")

if pilihan in ('1', '2'):
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print(f"Hasil: {angka1} + {angka2} = {angka1 + angka2}")
    elif pilihan == '2':
        print(f"Hasil: {angka1} - {angka2} = {angka1 - angka2}")
else:
    print("Pilihan tidak valid!")
