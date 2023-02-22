bilet = input("Введите номер билета: ")
if int(bilet[0]) + int(bilet[1]) + int(bilet[2]) == int(bilet[3]) + int(bilet[4]) + int(bilet[5]):
    print("Твой билет счастливый! Гони скорее в казино.")
else:
    print("Печалька, но не смертелька. Твой билет обычный.")