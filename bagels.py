import random
def getSecretNum(numDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return '\n¡Felicitaciones!\n¡Lo encontraste!'
   
    clue = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagels'

    clue.sort()
    return ' '.join(clue)

def isOnlyDigits(num):
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def playAgain():
    print('\n¿Querés jugar de nuevo? (si o no)')
    return input().lower().startswith('s')

NUMDIGITS = 3
MAXGUESS = 10

print('\nVoy a pensar en un número de %s dígitos y deberás adivinar cual es.' % (NUMDIGITS))
print('\nLuego de cada intento te daré las siguientes pistas:\n\n')
print('Cuando digo:    Significa:')
print('Pico            Un dígito es correcto, pero no está en su lugar.')
print('Fermi           Un dígito es correcto y está en su lugar.')
print('Bagels          Ningún dígito es correcto.')

while True:
    secretNum = getSecretNum(NUMDIGITS)
    print('\nEstoy pensando un número. Tenés %s intentos para descubrirlo.' % (MAXGUESS))

    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess = ''
        while len(guess) != NUMDIGITS or not isOnlyDigits (guess):
            print('Intento #%s: ' % (numGuesses))
            guess = input()

        clue = getClues(guess, secretNum)
        print(clue)
        numGuesses += 1

        if guess == secretNum:
            break
        if numGuesses > MAXGUESS:
            print('\nTe quedaste sin intentos.\nLa respuesta era %s.' % (secretNum))

    if not playAgain():
        break
