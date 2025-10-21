class Node:
    def __init__(self, jenis, nama, no_antrian):
        self.jenis = jenis
        self.nama = nama
        self.no_antrian = no_antrian
        self.prev = None
        self.next = None

class No_antri:
    def __init__(self, max_nomor):
        self.max_nomor = max_nomor
        self.next_number = 1
        self.ava_num = []
        
    def ambil_nomor(self):
        if self.ava_num:
            nomor = self.ava_num.pop(0)
        else:
            nomor = self.next_number
            self.next_number += 1
            if self.next_number > self.max_nomor:
                self.next_number = 1
        return nomor

    def kembali_nomor(self, nomor):
        if nomor not in self.ava_num:
            self.ava_num.append(nomor)
            self.ava_num.sort()

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        self.nomor = No_antri(max_nomor = 5)

    def isempty(self):
        return self.front is None

    def input_pasien_umum(self):
        print("\nTentukan jenis pasien")
        print("Khusus / Umum")
        jenis = input("Input jenis kondisi pasien: ").upper()
        nama = input("Input nama pasien: ")

        no_antrian = self.nomor.ambil_nomor()
        newnode = Node(jenis, nama, no_antrian)

        print("\n=== Data Pasien ===")
        print(f"Jenis Pasien: {newnode.jenis}")
        print(f"Nama Pasien: {newnode.nama}")
        print(f"Nomor Antrian: {newnode.no_antrian}\n")
        
        if newnode.jenis == "KHUSUS":
            if self.isempty():
                self.front = self.rear = newnode
            else:
                newnode.next = self.front
                self.front.prev = newnode
                self.front = newnode
        else:
            if self.isempty():
                self.front = self.rear = newnode
            else:
                newnode.prev = self.rear
                self.rear.next = newnode
                self.rear = newnode
            
        self.size += 1
        print("Data berhasil ditambahkan")

    def proses_pasien(self):
        if self.isempty():
            print("Belum ada antrian")
            return None
        
        temp_del = self.front
        
        print("\n=== Data Pasien ===")
        print(f"Jenis Pasien: {temp_del.jenis}")
        print(f"Nama Pasien: {temp_del.nama}")
        print(f"Nomor Antrian: {temp_del.no_antrian}\n")
        
        self.nomor.kembali_nomor(temp_del.no_antrian)
        
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        
        self.size -= 1
        print("Pasien telah berhasil diproses")

    def cancel_pasien(self):
        if self.isempty():
            print("Belum ada antrian")
            return None
        
        temp_del = self.rear
        
        print("\n=== Data Pasien ===")
        print(f"Jenis Pasien: {temp_del.jenis}")
        print(f"Nama Pasien: {temp_del.nama}")
        print(f"Nomor Antrian: {temp_del.no_antrian}\n")
        
        self.nomor.kembali_nomor(temp_del.no_antrian)
        
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        
        self.size -= 1
        print("Pasien telah berhasil dicancel")
    
    def tampilkan_pasien(self):
        if self.isempty():
            print("Belum ada antrian")
            return None
        
        print("=== Antrian dari Depan ===")
        temp = self.front
        while temp:
            print("\n=== Data Pasien ===")
            print(f"Jenis Pasien: {temp.jenis}")
            print(f"Nama Pasien: {temp.nama}")
            print(f"Nomor Antrian: {temp.no_antrian}\n")
            temp = temp.next
        print("None")
        print(f"Total Antrian: {self.size}\n")

def main():
    deque = Deque()
    
    while True:
        print("\n+== Rumah Sakit Tulalit ===")
        print("| 1. Input Pasien")
        print("| 2. Proses Pasien")
        print("| 3. Cancel Pasien")
        print("| 4. Lihat Antrian")
        print("| 5. Keluar")
        menu = int(input("| Input Pilihan: "))
        
        if menu == 1:
            deque.input_pasien_umum()
            if deque.front.jenis == 'KHUSUS':
                deque.proses_pasien()
        elif menu == 2:
            deque.proses_pasien()
        elif menu == 3:
            deque.cancel_pasien()
        elif menu == 4:
            deque.tampilkan_pasien()
        elif menu == 5:
            print("Terima Kasih - Sehat Selalu ^_^")
            break
        else:
            print("Pilihan Tidak ada")


if __name__ == "__main__":
    main()