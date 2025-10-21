# ==== Class Node / Linked List ====
class Node:
    def __init__(self, ID, bank, rek, nominal, biaya):
        self.ID = ID
        self.bank = bank
        self.rek = rek
        self.nominal = nominal
        self.biaya = biaya
        self.total_transaksi = nominal + biaya
        self.next = None  # cukup next

# ==== Global Variables ====
head = None
tail = None
kode = 0
saldo = 0
sisa = 0

# ==== Helper Functions ====
def isempty():
    return head is None

# ==== Tambah Saldo ====
def tambah_saldo():
    global saldo, sisa
    nominal = int(input("Masukkan jumlah saldo: "))
    saldo += nominal
    sisa += nominal
    print(f"Saldo berhasil ditambahkan. Saldo sekarang: Rp{sisa}\n")

# ==== Transfer ====
def transfer():
    global head, tail, kode, sisa

    bank_list = {"BCA":500, "BRI":1000, "BNI":1200, "Mandiri":1500, "CIMB":2000}

    # Pilih bank
    while True:
        bank = input("Pilih Bank (BCA/BRI/BNI/Mandiri/CIMB): ")
        if bank in bank_list:
            biaya = bank_list[bank]
            break
        print("Bank tidak ada, ulangi.")
    
    rek = input("Masukkan nomor rekening tujuan: ")

    # Masukkan nominal transfer
    while True:
        nominal = int(input("Masukkan nominal transfer: "))
        total = nominal + biaya
        if total > sisa:
            print("Saldo Tidak Cukup!")
        else:
            sisa -= total
            break

    # Buat node baru
    kode += 1
    newnode = Node(kode, bank, rek, nominal, biaya)

    # Sambungkan ke linked list
    global head, tail
    if isempty():
        head = tail = newnode
    else:
        tail.next = newnode
        tail = newnode

    print("=== Transaksi Berhasil! ===")
    print(f"Kode Unik: {newnode.ID}")
    print(f"Bank     : {newnode.bank}")
    print(f"Rekening : {newnode.rek}")
    print(f"Nominal  : Rp{newnode.nominal}")
    print(f"Admin Fee: Rp{newnode.biaya}")
    print(f"Total    : Rp{newnode.total_transaksi}")
    print(f"Sisa Saldo: Rp{sisa}\n")

# ==== Cetak Riwayat ====
def cetak_riwayat():
    if isempty():
        print("Riwayat transaksi kosong.\n")
        return
    
    print("=== Riwayat Transaksi ===")
    temp = head
    while temp:
        print(f"{temp.ID} | {temp.bank} | Rek: {temp.rek} | Nominal: Rp{temp.nominal} | Admin: Rp{temp.biaya} | Total: Rp{temp.total_transaksi}")
        temp = temp.next
    print()

# ==== Hapus Transaksi ====
def hapus_transaksi():
    global head, tail
    if isempty():
        print("Data transaksi belum ada.\n")
        return
    
    X = int(input("Masukkan kode transaksi yang ingin dihapus: "))
    temp = head
    prev = None
    found = False
    while temp:
        if temp.ID == X:
            found = True
            # Hapus node
            if prev is None:  # head
                head = temp.next
                if head is None:
                    tail = None
            else:
                prev.next = temp.next
                if temp.next is None:  # hapus tail
                    tail = prev
            print(f"Transaksi dengan kode {X} berhasil dihapus.\n")
            break
        prev = temp
        temp = temp.next
    if not found:
        print("Data transaksi tidak ada.\n")

# ==== Cek Saldo ====
def cek_saldo():
    print(f"Saldo saat ini: Rp{sisa}\n")

# ==== Menu Utama ====
def main():
    while True:
        print("=== Sistem Top Up Bank ===")
        print("1. Tambah Saldo")
        print("2. Transfer ke Bank")
        print("3. Cetak Riwayat")
        print("4. Hapus Transaksi")
        print("5. Cek Saldo")
        print("6. Keluar")
        pilih = input("Pilih Menu: ")

        if pilih == "1":
            tambah_saldo()
        elif pilih == "2":
            transfer()
        elif pilih == "3":
            cetak_riwayat()
        elif pilih == "4":
            hapus_transaksi()
        elif pilih == "5":
            cek_saldo()
        elif pilih == "6":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak ada\n")

# ==== Jalankan Program ====
if __name__ == "__main__":
    main()
