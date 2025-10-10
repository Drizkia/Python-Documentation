# set
# duplikat auto delete (mutable)
def SET():
    a = {1, 2, 3}
    b = {3, 4, 5}
    # .add()
    # .pop() or .remove() or .discard()
    # gabung, irisan, selisih
        # (a | b) = union {1, 2, 3, 4, 5}
        # (a & b) = intersection {3}
        # (a - b) = difference {1, 2}
        # (a ^ b) = symetric diff {1, 2, 4, 5}
    # cek anggota
        # (2 in a) = True
        # (7 not in a) = True
        
    list = [1, 2, 2, 3]
    no_dup = set(list) # untuk ubah list ke tuple 

#TUPLE
# koleksi elemen gabisa diubah (immutable)
def TUPLE():
    t = (1, 2, 3, 4)
    y = (0, 9, 8, 5)
    # Akses elemen
        # print(t[0]) # 1
    # Slice
        # print(t[1:3]) # (2, 4) 
    # Gabung tuple
        # ptiny(x = t + y)
    # Ulang tuple
        # print(t * 3)
    # Cek keanggotaan
        # print(2 in t) # True
    # Cek berapa muncul
        # .count()
    # Kembaliin index pertama
        # .index()

    list = [3, 1, 2]
    t2 = tuple(list)
    print(t2)

# DICTIONARY
# Pasangan {key : value}
def DICT():
    d = {"nama": "Dimas", "umur": 20}
    print(d["umur"]) # 20
    # Hapus item
        # del d["hobi"]
        # .pop("umur")
    # Cek key
        # print("nama" in d)
    # output
        # d.keys()
        # d.values()
        # d.items()
    pass