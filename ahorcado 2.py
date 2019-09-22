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

words = {'Colores':'rojo azul amarillo violeta celeste marron beige cremita salmon lila naranja negro blanco gris turquesa rosa'.split(),
'Formas':'cuadrado rectangulo circulo hexagono pentagono elipse triangulo octogono'.split(),
'Frutas':'manzana naranja limon anana kiwi coco cereza ciruela frambuesa higo maqui pera banana'.split(),
'Animales':'perro gato chancho comadreja tigre puma leon condor paloma gallina vaca caballo bufalo elefante mono rata pantera gorrion hipopotamo murcielago chimango peludo mulita burro mula huron tortuga tiburon araña tarantula zebra'.split(),
'Cosas':'casa mesa silla vidon frasco estufa ladrillo madera tabla computadora telefono televisor vaso tornillo balde cajon ventana clavo caño'.split(),
'Emociones':'amor cariño ira rencor estima alegria tristeza ternura ansiedad frustracion enojo afecto'.split(),
'Acciones':'caricia beso abrazo sosten ayuda piña trompada patada masaje empujon caminar correr saltar volar decir hacer sentir morder'.split(),
'Seres':'niña niño viejo vieja abuelo abuela mama papa tio hermano hermana elfo hada enano duende troll mago'.split()}

def getRandomWord(wordDict):
	#Retorna una palabra al azar.
    wordKey = random.choice(list(wordDict.keys()))

    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]

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
secretWord, secretKey = getRandomWord(words)
gameIsDone = False

while True:
	print('La palabra secreta pertenece a la categoría: ' + secretKey)
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
			secretWord, secretKey = getRandomWord (words)
		else:
			break

