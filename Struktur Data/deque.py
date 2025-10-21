# ==== Class Node untuk Deque ====
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # pointer ke node sebelumnya
        self.next = None  # pointer ke node setelahnya

# ==== Deque (Double-Ended Queue) ====
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def isempty(self):
        return self.size == 0
    
#! INSERT DEPAN
    def insert_front(self, data):
        newnode = Node(data)
        
        if self.isempty():
            self.front = self.rear = newnode
        else:
            newnode.next = self.front
            self.front.prev = newnode
            self.front = newnode
        
        self.size += 1
        print(f"Data '{data}' berhasil ditambahkan di DEPAN.\n")
        return True

#! INSERT BELAKANG
    def insert_rear(self, data):
        newnode = Node(data)
        
        if self.isempty():
            self.front = self.rear = newnode
        else:
            newnode.prev = self.rear
            self.rear.next = newnode
            self.rear = newnode
        
        self.size += 1
        print(f"Data '{data}' berhasil ditambahkan di BELAKANG.\n")
        return True

#! HAPUS DEPAN
    def delete_front(self):
        if self.isempty():
            print("Deque kosong! Tidak ada data untuk dihapus.\n")
            return None
        
        removed_data = self.front.data
        
        if self.front == self.rear:  # hanya 1 node
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        
        self.size -= 1
        print(f"Data '{removed_data}' berhasil dihapus dari DEPAN.\n")
        return removed_data

#! HAPUS BELAKANG
    def delete_rear(self):
        if self.isempty():
            print("Deque kosong! Tidak ada data untuk dihapus.\n")
            return None
        
        removed_data = self.rear.data
        
        if self.front == self.rear:  # hanya 1 node
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        
        self.size -= 1
        print(f"Data '{removed_data}' berhasil dihapus dari BELAKANG.\n")
        return removed_data

#! AMBIL NILAI DARI DEPAN
    def get_front(self):
        if self.isempty():
            print("Deque kosong!\n")
            return None
        return self.front.data

#! AMBIL NILAI DARI BELAKANG
    def get_rear(self):
        if self.isempty():
            print("Deque kosong!\n")
            return None
        return self.rear.data

#! DISPLAY
    def display(self):
        if self.isempty():
            print("Deque kosong.\n")
            return
        
        print("=== Isi Deque (Depan -> Belakang) ===")
        temp = self.front
        while temp:
            print(f"[{temp.data}]", end=" <-> ")
            temp = temp.next
        print("None")
        print(f"Ukuran: {self.size}\n")

#! DISPLAY TERBALIK
    def display_reverse(self):
        if self.isempty():
            print("Deque kosong.\n")
            return
        
        print("=== Isi Deque (Belakang -> Depan) ===")
        temp = self.rear
        while temp:
            print(f"[{temp.data}]", end=" <-> ")
            temp = temp.prev
        print("None")
        print(f"Ukuran: {self.size}\n")

def main():
    deque = Deque()
    
    while True:
        print("=== Deque Menu ===")
        print("1. Insert Front (Tambah di depan)") #todo Enque-Front
        print("2. Insert Rear (Tambah di belakang)") #todo Enque-Rear
        print("3. Delete Front (Hapus dari depan)") #todo Deque-Front
        print("4. Delete Rear (Hapus dari belakang)") #todo Deque-Rear

        print("5. Get Front (Lihat data depan)") #todo Display 1 Data Front
        print("6. Get Rear (Lihat data belakang)") #todo Display 1 Data Rear

        print("7. Display (Tampilkan Depan->Belakang)") #todo Display full front
        print("8. Display Reverse (Tampilkan Belakang->Depan)") #todo Display full rear
        print("9. Keluar")

        pilih = input("Pilih Menu: ")

        if pilih == "1":
            data = input("Masukkan data: ")
            deque.insert_front(data)
        elif pilih == "2":
            data = input("Masukkan data: ")
            deque.insert_rear(data)
        elif pilih == "3":
            deque.delete_front()
        elif pilih == "4":
            deque.delete_rear()
        elif pilih == "5":
            front_data = deque.get_front()
            if front_data:
                print(f"Data di depan: {front_data}\n")
        elif pilih == "6":
            rear_data = deque.get_rear()
            if rear_data:
                print(f"Data di belakang: {rear_data}\n")
        elif pilih == "7":
            deque.display()
        elif pilih == "8":
            deque.display_reverse()
        elif pilih == "9":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak ada\n")

if __name__ == "__main__":
    main()