import random
HANGMANPICS = ['''


    +---+
    |   |
        |
        |
        |
        |
        |
   ========''', '''


    +---+
    |   |
    0   |
        |
        |
        |
        |
   ========''', '''


    +---+
    |   |
    0   |
    |   |
        |
        |
        |
   ========''', '''


    +---+
    |   |
    0   |
    |   |
   /    |
        |
        |
   ========''', '''


    +---+
    |   |
    0   |
    |   |
   / \	|
        |
        |
   ========''', '''


    +---+
    |   |
    0   |
   /|   |
   / \	|
        |
        |
   ========''', '''


    +---+
    |   |
    0   |
   /|\	|
   / \	|
        |
        |
   ========''', '''


    +---+
    |   |
   (0   |
   /|\	|
   / \	|
        |
        |
   ========''', '''


    +---+
    |   |
   (0)  |
   /|\	|
   / \	|
        |
        |
   ========''']

words = 'camello tortuga erizo bife chancho peludo rata chinchulin socotroco pituto flauta alcornoque retama tripas rotura murcielago dinosaurio persona avion television computadora prismaticos telefono sanguche alivio pedo vigornia preludio libelula catarata rimbombante plesiosaurio tiburon mar vid sed perdiste castaña pestaña araña migraña lasagna gnomo enano elfo duende tarantula casa pueblo barro arcilla estufa lechuza ventana mesa telefono hombre mujer niño niña perro vaca cielo nube estrella planeta tierra pachamama ladrillo arena ilusion emocion amor amantes cariño abrazo mente corazon amable ayuda obra trabajo reloj metal silla vidon guitarra bajo contrabajo charango violin viola tambor ukelele automovil camion tren'.split()

def getRandomWord(wordList):
	#Retorna una palabra al azar.
	wordIndex = random.randint(0, len(wordList) - 1)
	return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
	print(HANGMANPICS[len(missedLetters)])
	print()

	print('Letras erradas:', end=' ')
	for letter in missedLetters:
		print(letter, end=' ')
	print()

	blanks = '_' * len(secretWord)
	
	for i in range(len(secretWord)): #Reemplaza espacios por letras adivinadas
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
	for letter in blanks: #Muestra la palabra con espacios entre las letras
		print(letter, end=' ')
	print()

def getGuess(alreadyGuessed):
	#Devuelve la letra ingresado. Esta linea se asegura que se haya ingresado una letra y no otra cosa.
	while True:
		print('Ingresá una letra.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print('Por favor, ingresá una sola letra')
		elif guess in alreadyGuessed:
			print('Esa ya la elegiste. Elegí otra.')
		elif guess not in 'abcdefghijklmnñopqrstuvwxyz':
			print('Por favor, ingresá una LETRA')
		else:
			return guess

def playAgain():
	#Devuelve verdadero si quiere jugar de nuevo, sino devuelve Falso.
	print('¿Querés jugar de nuevo? (si o no)')
	return input().lower().startswith('s')

print('C O L G A D O')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
	displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

	#Dejar que el jugador tipee una letra
	guess = getGuess(missedLetters + correctLetters)

	if guess in secretWord:
		correctLetters = correctLetters + guess

		# Chequear si ganó
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print('\n\n¡Si!, la palabra secreta es ' + '\"' + secretWord + '\"' + '\n\n¡Ganaste!\n\n')
			gameIsDone = True
	else:
		missedLetters = missedLetters + guess

			#Chequear si intentó muchas veces y perdió
		if len(missedLetters) == len(HANGMANPICS) -1:
			displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
			print('Te quedaste sin chances\nDespués de '+ str(len(missedLetters)) + ' letras erradas y ' + str(len(correctLetters)) + ' letras acertadas, la palabra era "' + secretWord + '"')
			gameIsDone = True 

	# Preguntar si quiere jugar de nuevo, pero solo si el juego acabó

	if gameIsDone:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameIsDone = False
			secretWord = getRandomWord (words)
		else:
			break

