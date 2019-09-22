import random
import time

def displayIntro():
	print('Estás en un planeta lleno de dragones, adelante tuyo hay dos cuevas. \nEn una cueva vive un dragón amable que compartiría su tesoro contigo; \nen la otra cueva  vive un dragón malo y hambriento, \nque te comería al instante antes de que pudieras gritar.')
	print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('¿En que cueva vas a entrar (1 o 2)?')
		cave = input()

	return cave

def checkCave(chosenCave):
	print('Te aproximas a la cueva lentamente...')
	time.sleep(2)
	print('...es oscura y tenebrosa...')
	time.sleep(2)
	print('De repente un dragón salta delante tuyo, abre su boca enorme y...')
	print()
	time.sleep(4)

	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('...te dice "¡Que bueno que me visites, compartamos mi tesoro!"')
	else:
		print('...te traga en un solo bocado.')
		time.sleep(3)		
		print('''
    .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................
		''')	

playAgain = 'si'
while playAgain == 'si' or playAgain == 's':

	displayIntro()
	
	caveNumber = chooseCave()

	checkCave(caveNumber)

	print('¿Querés jugar de nuevo? (si o no)')
	playAgain = input()

