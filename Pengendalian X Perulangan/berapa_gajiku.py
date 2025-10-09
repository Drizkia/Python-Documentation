NIM = 123240123
PASS = 'bubadibako'

kesempatan = 5
def login(kesempatan):
    while True:
        if kesempatan == 0:
            print("Kesempatan Habis!")
            break
        x = int(input("Masukkan Username : "))
        y = input("Masukkan Password : ")
        kesempatan -= 1
        if x == NIM and y == PASS:
            print("Welcome")
            break
        else:
            print("Username atau Password salah!")
            print(f'Kesempatan tersisa: {kesempatan}')

def input_gaji(gaji):
    while True:
        masuk = int(input("Berapa kali masuk: "))
        if masuk > 26:
            print("Maksimal 26 Hari!")
        else:
            break
    
    while True:
        cuti = int(input("Berapa kali cuti: "))
        if cuti > 4:
            print("Maksimal 4 Hari!")
        else:
            break
    total_masuk = masuk - cuti
    return total_masuk

def sub_total(total_masuk, gaji):
    sub_gaji = total_masuk * gaji
    sub_gaji += 500000
    keluarga = input("Apakah sudah berkeluarga: ").lower()
    if keluarga == 'y':
        sub_gaji += 500000
    else:
        sub_gaji
    sub_gaji -= 200000
    
    print(sub_gaji)

login(kesempatan)
jabatan = input("Masukkan jabatan : ").upper()
if jabatan == 'CEO':
    gaji = 20000000
    total_masuk = input_gaji(gaji)
    sub_total(total_masuk, gaji)
elif jabatan == 'SUPERVISOR':
    gaji = 15000000
    total_masuk = input_gaji(gaji)
    sub_total(total_masuk, gaji)
elif jabatan == 'WEB DEVELOP':
    gaji = 8500000
    total_masuk = input_gaji(gaji)
    sub_total(total_masuk, gaji)
elif jabatan == 'CS':
    gaji = 4000000
    total_masuk = input_gaji(gaji)
    sub_total(total_masuk, gaji)
elif jabatan == 'OB':
    gaji = 3000000
    total_masuk = input_gaji(gaji)
    sub_total(total_masuk, gaji)
