# Programming in Python 3, pag. 35
# Ejecutar:
# python sum2.py < sum2.dat
# El archivo "sum2.dat" brinda los datos de enteros para que el script realice los càlculos.

print()
print("Ingresa números enteros, cada uno seguido por la tecla Enter, o ^D o ^Z para terminar")
print()

total = 0
count = 0

while True:
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break
if count:
    print()
    print("Cantidad de enteros: ", count)
    print("Suma total: ", total)
    print("Promedio: ", total / count)
    print()
