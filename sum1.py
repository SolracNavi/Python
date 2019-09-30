# Programming in Python 3, pag. 34

print("Ingresa números enteros, cada uno seguido de Enter; o presiona Enter para terminar")
print()
total = 0
count = 0
while True:
    line = input("Entero: ")
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        total += number
        count += 1
    else:
        break

if count:
    print()
    print("Cantidad de números ingresados=", count)
    print("Suma total =", total)
    print("Promedio =", total / count)
    print()
