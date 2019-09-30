# Programming in Python 3, pag. 41
# Nùmeros Ascii tomados de: https://gist.github.com/yuanqing/ffa2244bd134f911d365
import sys

Zero = [" 0000 ", "00  00", "00  00", "00  00", " 0000 "]
One = ["1111  ", "  11  ", "  11  ", "  11  ", "111111"]
Two = [" 2222 ", "22  22", "   22 ", "  22  ", "222222"]
Three = [" 3333 ", "33  33", "   333", "33  33", " 3333 "]
Four = ["44  44", "44  44", "444444", "    44", "    44"]
Five = ["555555", "55    ", "55555 ", "    55", "55555 "]
Six = [" 6666 ", "66    ", "66666 ", "66  66", " 6666 "]
Seven = ["777777", "   77 ", "  77  ", " 77   ", "77    "]
Eight = [" 8888 ", "88  88", " 8888 ", "88  88", " 8888 "]
Nine = [" 9999 ", "99  99", " 99999", "    99", " 9999 "]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 5:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + "  "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <número>")
except ValueError as err:
    print(err, "in", digits)
