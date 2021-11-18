rata = float(input("Masukkan nilai rata-rata UG anda: "))
tts  = float(input("Masukkan nilai TTS anda: "))
tas  = float(input("Masukkan nilai TAS anda: "))
print("=========================")

nilai = ((rata*0.7)+(tts*0.15)+(tas*0.15))
print("Nilai anda: ",str(nilai))

if (rata < 0 or tts < 0 or tas < 0):
    print("Maaf nilai yang anda inputkan tidak boleh kurang dari nol")
elif nilai < 45:
    print("Nilai huruf anda: E")
elif nilai < 55:
    print("Nilai huruf anda: D")
elif nilai < 60:
    print("Nilai huruf anda: C")
elif nilai < 65:
    print("Nilai huruf anda: C+")
elif nilai < 70:
    print("Nilai huruf anda: B-")
elif nilai < 75:
    print("Nilai huruf anda: B")
elif nilai < 80:
    print("Nilai huruf anda: B+")
elif nilai < 85:
    print("Nilai huruf anda: A-")
else:
    print("Nilai huruf anda: A")







