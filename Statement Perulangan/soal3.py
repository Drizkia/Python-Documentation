umur = int(input("Masukkan umur: "))
if umur <= 5:
    print("Bayi")
elif umur >= 6 and umur <= 10:
    print("Anak")
elif umur >= 11 and umur <= 17:
    print("Remaja")
elif umur >= 18 and umur <= 40:
    print("Dewasa")
else:
    print("Lansia")
