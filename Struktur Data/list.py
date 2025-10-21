barang = []

def display():
    print("=== DAFTAR BARANG ===")
    if len(barang) == 0:
        print("Belum ada data!")
    else:
        for i in  range(len(barang)):
            print(f"Barang : {i+1} = {barang}")

def tambah_satu():
    x = input("Masukkan barang: ")
    barang.append(x)
    display()

def tambah_banyak():
    y = int(input("Berapa barang: "))
    temp = []
    for i in range(y):
        x = input(f"Masukkan barang ke-{i+1}: ")
        temp.append(x)
    barang.extend(temp)
    display()

def sisip_posisi():
    y = int(input("Akan dimasukkan pada list berapa: "))
    x = input("Masukkan barang: ")
    barang.insert(y, x)
    display()

def hapus_barang_by():
    x = input("Masukkan nama barang: ")
    barang.remove(x)
    display()

def hapus_barang_last():
    barang.pop()
    display()

while True:
    print("============== MENU TOKO ================")
    print('A. Tambah satu barang')
    print('B. Tambah banyak barang')
    print('C. Sisipkan barang diposisi tertentu')
    print('D. Hapus barang berdasarkan nama')
    print('E. Hapus barang terakhir')
    print('F. Tampilkan semua barang')
    print('G. Urutkan barang (A-Z)')
    print('H. Balik urutan barang')
    print('I. Hapus semua data')
    print('J. Keluar')
    print('========================================')
    menu = input('Masukkan menu: ').upper()
    print("\n")
    if menu == 'A':
        tambah_satu()
    elif menu == 'B':
        tambah_banyak()
    elif menu == 'C':
        sisip_posisi()
    elif menu == 'D':
        hapus_barang_by()
    elif menu == 'E':
        hapus_barang_last()
    elif menu == 'F':
        display()
    elif menu == 'G':
        barang.sort()
        display()
    elif menu == 'H':
        barang.reverse()
        display()
    elif menu == 'I':
        konfirmasi = input("Yakin hapus semua data? (y/n)").lower()
        if konfirmasi == 'y':
            barang.clear()
            print("Semua data sudah berhasil dihapus")
        display()
    elif menu == 'J':
        break