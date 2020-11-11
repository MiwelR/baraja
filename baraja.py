import random

#palos = ['o', 'c', 'e', 'b']
#numeros = ['A', '1', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']


def creaBaraja(palos, numeros):
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero + palo)

    return baraja

def intercambio(valor1, valor2):
    aux = valor1
    valor1 = valor2
    valor2 = aux
    return valor1, valor2


def barajar(lista_de_cartas):
    for i in range(len(lista_de_cartas)):
        nueva_pos = random.randrange((len(lista_de_cartas)))
        '''
        Intercambio de cartas: técnica "vaso vacío"
        '''
        aux = lista_de_cartas[nueva_pos]
        lista_de_cartas[nueva_pos] = lista_de_cartas[i]
        lista_de_cartas[i] = aux
    return lista_de_cartas

