print("############################")
print("Kalkulator Advance Sederhana")
print("############################")
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")
menu = int(input("Masukkan menu yang anda pilih: "))

if menu == 1:
    dibagi = float(input("Masukkan bilangan yang ingin dibagi: "))
    pembagi = float(input("Masukkan bilangan pembagi: "))
    hasil = (dibagi % pembagi)
    print("Sisa hasil bagi",dibagi,"dibagi dengan",pembagi,"adalah",hasil)
elif menu == 2:
     dibagi = float(input("Masukkan bilangan yang ingin dibagi: "))
     pembagi = float(input("Masukkan bilangan pembagi: "))
     hasil = (dibagi // pembagi)
     print("hasil pembagian",dibagi,"dibagi dengan",pembagi,"dibulatkan kebawah adalah",hasil)
elif menu == 3:
     akar = float(input("Masukkan bilangan yang ingin dicari akar kubiknya: "))
     hasil = akar ** (1/3)
     print("Akar kubik dari",akar,"adalah",hasil)
else:
    print("Menu yang anda pilih tidak tersedia")