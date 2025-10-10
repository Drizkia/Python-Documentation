# Buat list kuadrat 0-4
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Ambil angka genap saja
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Buat list huruf kapital dari string
words = "python"
caps = [c.upper() for c in words]
print(caps)  # ['P', 'Y', 'T', 'H', 'O', 'N']

# [expression for item in iterable if condition]


# sequence[start:stop:step]