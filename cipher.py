# Caesar Cipher

MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('¿Querés encriptar, desencriptar, o aplicar fuerza bruta a un mensaje?')
        mode = input().lower()
        if mode in 'encriptar e desencriptar d bruta b'.split():
            return mode
        else:
            print ('Ingresa "encriptar" o "e", o "desencriptar" o "d", o "bruta" o "b".')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    key = 0
    while True:
        print ('Ingresa el número de llave. (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage (mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()

print('Tu texto traducido es:')
if mode [0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))

