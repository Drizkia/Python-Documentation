cuaca = input("Cuaca hari ini apa: ").lower()
if cuaca == 'hujan':
    suhu = int(input("Suhu hari ini: "))
    if suhu <= 20:
        print("Payung dan Jaket")
    else:
        print('Payung')
elif cuaca == 'panas':
    suhu = int(input("Suhu hari ini: "))
    if suhu >= 30:
        print("Sunscreen dan Jaket")
    elif suhu >= 21 and suhu <= 29:
        print("Sunscreen dan baju Hem")
    else:
        print('Sunscreen')
