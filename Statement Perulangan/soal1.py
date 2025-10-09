HARGA = 80000

baju = int(input("Ingin membeli berapa baju: "))

total_harga = HARGA * baju
if total_harga >= 300000 and total_harga <= 499999:
    diskon = int(total_harga * 0.1)
    print(f"Total harga sebelum diskon: {total_harga}")
    print(f"Diskon anda: {diskon}")
    total_harga -= diskon
    print(f"Total harga anda: {total_harga}")
elif total_harga >= 500000:
    diskon = int(total_harga * 0.2)
    print(f"Total harga sebelum diskon: {total_harga}")
    print(f"Diskon anda: {diskon}")
    total_harga -= diskon
    print(f"Total harga anda: {total_harga}")
else:
    print(f"Total harga anda {total_harga}")
