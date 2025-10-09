umur = int(input("Masukkan umur : "))

if umur >= 17:
    ktp = input("Apakah anda sudah memiliki KTP(y/n) : ").lower()
    if ktp == 'y':
        print("Budi memenuhi syarat membuat SIM")
    else:
        print("Budi belum bisa membuat SIM karna tidak punya KTP")
else:
    print("Budi belum cukup umur untuk membuat SIM")