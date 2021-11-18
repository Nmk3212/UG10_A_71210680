pilihan = input("Mendatar/Menurun?: ")

if pilihan == "Mendatar":
    kolom = int(input("Masukkan kolom: "))
    print("#" * kolom)
elif pilihan == "Menurun":
    baris = int(input("Masukkan baris: "))
    print("*\n" * baris)
else:
    print("Pola tidak dikenali")