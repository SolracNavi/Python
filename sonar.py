# Sonar

import random
import sys

def drawBoard(board):
    hline = '    '
    for i in range(1, 6):
        hline += (' ' * 9) + str(i)

    print(hline)
    print('   ' + ('0123456789' * 6))
    print()

    for i in range(15):
        if i < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        print('%s%s %s %s' % (extraSpace, i, getRow (board, i), i))
    print()
    print('   ' + ('0123456789' * 6))
    print(hline)

def getRow(board, row):
    boardRow = ''
    for i in range(60):
        boardRow += board[i][row]
    return boardRow

def getNewBoard():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('¬')
    return board

def getRandomChests(numChests):
    chests = []
    for i in range(numChests):
        chests.append([random.randint(0, 59), random.randint(0, 14)])
    return chests

def isValidMove(x, y):
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    if not isValidMove(x, y):
        return False
    smallestDistance = 100
    for cx, cy in chests:
        if abs(cx - x) > abs(cy - y):
            distance = abs(cx -x)
        else:
            distance = abs(cy - y)
      
        if distance < smallestDistance:
            smallestDistance = distance

    if smallestDistance == 0:
        chests.remove([x, y])
        return '¡Encontraste un cofre del tesoro!'
    else:
        if smallestDistance < 10:
             board[x][y] = str(smallestDistance)
             return 'Tesoro detectado a una distancia de %s desde el sonar.' % (smallestDistance)
        else:
            board[x][y] = 'O'
            return 'El sonar no detectó nada. Todos los tesoros están fuera del rango.'

def enterPlayerMove():
    print('¿Donde querés dejar el próximo sonar? (0-59 0-14) (o tipea quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('¡Gracias por jugar!')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move [1].isdigit() and isValidMove(int(move[0]), int(move[1])):
            return [int(move[0]), int(move[1])]
        print('Ingresá un número del 0 al 59, un espacio, y después un número del 0 al 14.')

def playAgain():
    print('¿Querés jugar de nuevo? (si o no)')
    return input().lower().startswith('s')

def showInstructions():

    print('''Instrucciones:
Sos el capitan del Simón, un barco cazador de tesoros.
Tu misión actual es encontrar tres tesoros que están 
hundidos en esta parte del océano y recuperarlos.

Para jugar, entra las coordenadas del lugar donde
quieres dejar un sonar. El artefacto puede informarte
a que distancia está el cofre más cercano a su posición.

Por ejemplo: la d en la imágen de abajo muestra
donde fue dejado el sonar, y los numeros 2
representan distancias de 2 desde el sonar.
Los 4 representan distancias de 4 desde el dispositivo.

    444444444
    4       4
    4 22222 4
    4 2   2 4
    4 2 d 2 4
    4 2   2 4
    4 22222 4
    4       4
    444444444

Presiona enter para continuar...''')

    input()
    
    print('''Otro ejemplo: aquí vemos un cofre del tesoro
(la letra c) localizado a una distancia de 2 desde
el sonar (la letra d):

    22222
    c   2
    2 d 2
    2   2
    22222

El punto donde el sonar fue dejado será
maracado con un número 2.

El cofre del tesoro no tiene movimiento. El sonar
puede detectar un cofre a una distancia de 9.
Si todos los cofres estan fuera del rango, el
punto donde está el sonar se marcará
con un número 0.

Si un sonar es dejado directamente sobre un cofre 
habrás descubierto la localización del tesoro
y será colectado. El sonar permanecerá allí.

Cuando recojas un cofre, todos los sonares se
actualizarán para encontrar el próximo
cofre más cercano.

Presiona enter para continuar...''')
    input()
    print()


print('¡S O N A R!')
print()
print('¿Querés leer las instrucciones? (si o no)')
if input().lower().startswith('s'):
    showInstructions()

while True:
    sonarDevices = 16
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []
#    import pdb; pdb.set_trace()
    while sonarDevices > 0:
        if sonarDevices > 1: extraSsonar = 's'
        else: extraSsonar = ''
        if len(theChests) > 1: extraSchest = 's'
        else: extraSchest = ''
        print('Tenés %s dispositivo%s sonar disponible%s. Quedan %s cofre%s del tesoro.' % (sonarDevices, extraSsonar, extraSsonar, len(theChests), extraSchest))

        x, y = enterPlayerMove()
        previousMoves.append([x, y])

        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue
        else:
            if moveResult == '¡Encontraste un cofre del tesoro!':
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)

        if len(theChests) == 0:
            print('¡Encontraste todos los cofres del tesoro!, ¡bien jugado!, ¡felicitaciones!')
            break
        sonarDevices -= 1
    if sonarDevices == 0:
        print('¡Nos quedamos sin sonares!, ya no podremos rescatar más cofres.')
        print('\nJuego terminado.')
        print('        Los cofres que quedaban estaban aquí:')
        for x, y in theChests:
            print('     %s, %s' % (x, y))

    if not playAgain():
        sys.exit()


