class Node:
    def __init__(self, jenis, nama, no_antrian):
        self.jenis = jenis
        self.nama = nama
        self.no_antrian = no_antrian
        self.prev = None
        self.next = None

class CircularQueue:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.queue = [None] * kapasitas
        self.front = -1
        self.rear = -1
        self.size = 0
    
    def isfull(self):
        return self.size == self.kapasitas

    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self, data):
        if self.front == -1:
            self.front = 0
            
        self.rear = (self.rear + 1) % self.kapasitas
        self.queue[self.rear] = data
        self.size += 1
        return True

    def nextDokter(self):
        dokter = self.queue[self.front]
        self.front = (self.front + 1) % self.kapasitas
        
        self.rear = (self.rear + 1) % self.kapasitas
        self.queue[self.rear] = dokter
        return dokter

    def tampilDokter(self):
        print("\n=== DAFTAR DOKTER ===")
        temp = self.front
        for i in range(self.size):
            print(f"{i+1}. {self.queue[temp]}")
            temp = (temp + 1) % self.kapasitas
        print()
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        self.nomor = 0

    def isempty(self):
        return self.front is None

    def input_pasien_umum(self):
        print("\nTentukan jenis pasien")
        print("Khusus / Umum")
        jenis = input("Input jenis kondisi pasien: ").upper()
        nama = input("Input nama pasien: ")
        self.nomor += 1
        newnode = Node(jenis, nama, self.nomor)

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

    def proses_pasien(self, queue_dokter):
        if self.isempty():
            print("\nBelum ada antrian")
            return None
        
        temp_del = self.front
        dokter = queue_dokter.nextDokter()
        
        print("\n=== Data Pasien ===")
        print(f"Jenis Pasien: {temp_del.jenis}")
        print(f"Nama Pasien: {temp_del.nama}")
        print(f"Nomor Antrian: {temp_del.no_antrian}")
        print(f"Ditangani oleh: {dokter}\n")
        
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        
        self.size -= 1
        print("Pasien telah berhasil diproses")

    def cancel_pasien(self):
        if self.isempty():
            print("\nBelum ada antrian")
            return None
        
        temp_del = self.rear
        
        print("\n=== Data Pasien ===")
        print(f"Jenis Pasien: {temp_del.jenis}")
        print(f"Nama Pasien: {temp_del.nama}")
        print(f"Nomor Antrian: {temp_del.no_antrian}\n\n")
        
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        
        self.size -= 1
        print("Pasien telah berhasil dicancel")
    
    def tampilkan_pasien(self):
        if self.isempty():
            print("\nBelum ada antrian")
            return None
        
        print("=== Antrian dari Depan ===")
        temp = self.front
        while temp:
            print("\n=== Data Pasien ===")
            print(f"Jenis Pasien: {temp.jenis}")
            print(f"Nama Pasien: {temp.nama}")
            print(f"Nomor Antrian: {temp.no_antrian}\n\n")
            temp = temp.next
        print(f"Total Antrian: {self.size}\n")

def main():
    deque = Deque()
    
    queue_dokter = CircularQueue(5)
    dokter_list = ['dr. Andini Pratiwi, Sp.A',
                    'dr. Alexsendriano, Sp.PD',
                    'dr. Clara Wijaya, Sp.KK',
                    'dr. Dimas Nugroho, Sp.B',
                    'dr. Eka Putri, Sp.OG']
    for dokter in dokter_list:
        queue_dokter.enqueue(dokter)
    
    while True:
        print("\n+== Rumah Sakit Tulalit ===")
        print("| 1. Input Pasien")
        print("| 2. Proses Pasien")
        print("| 3. Cancel Pasien")
        print("| 4. Lihat Antrian Pasien")
        print("| 5. Lihat Urutan Dokter")
        print("| 6. Keluar")
        menu = int(input("| Input Pilihan: "))
        
        if menu == 1:
            deque.input_pasien_umum()
            if deque.front.jenis == 'KHUSUS':
                deque.proses_pasien(queue_dokter)
        elif menu == 2:
            deque.proses_pasien(queue_dokter)
        elif menu == 3:
            deque.cancel_pasien()
        elif menu == 4:
            deque.tampilkan_pasien()
        elif menu == 5:
            queue_dokter.tampilDokter()
        elif menu == 6:
            print("Terima Kasih - Sehat Selalu ^_^")
            break
        else:
            print("Pilihan Tidak ada")

if __name__ == "__main__":
    main()