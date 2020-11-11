import baraja

palos = ['o', 'c', 'e', 'b']
numeros = ['A', '1', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']

baraja_uno = baraja.creaBaraja(palos, numeros)
print("Esta es la primera baraja: ", baraja_uno)

baraja_dos = baraja.creaBaraja(palos, numeros)
print("Esta es la segunda baraja: ", baraja_dos)
baraja.barajar(baraja_dos)
print("Esta es la segunda baraja desordenada: ", baraja_dos)