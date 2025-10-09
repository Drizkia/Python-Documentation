HARGA = 50000
def pesan():
    baju = int(input('\nBerapa baju: '))
    return baju

def total_pesan(baju):
    total = baju * HARGA
    if total >= 250000:
        diskon = int(baju * 0.25)
        total -= diskon
        print(f'Total anda: {total}\n')
    else:
        print(f'Total anda: {total}\n')

while True:
    menu = input('\nMasukkan menu: ').upper()

    if menu == 'A':
        baju = pesan()
    elif menu == 'B':
        if baju == 0:
            print('Belum ada data')
        else:
            total_pesan(baju)
    elif menu == 'C':
        print('Thank You')
        break
    else:
        print('Pilihan tidak ada')
