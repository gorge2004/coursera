import random
import math


def tirar_dados(start=1, end=6):
	
	return math.floor((random.random() * (end - start + 1))+ start) 


def jugar_dado():
	stopPlay = 'S'
	
	while True:
		dado_1 = tirar_dados()
		dado_2 = tirar_dados()
		print('valor del dado 1:',dado_1)
		print('valor del dado 2:',dado_2, ', La suma de ambos dados es:', dado_1 + dado_2, )
		stopPlay = input("desea continuar jugando?(S/N):")
		if stopPlay == 'N' or stopPlay == 'n':
			break


jugar_dado()
