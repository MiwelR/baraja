import baraja

baraja_uno = baraja.creaBaraja()
print("Esta es la primera baraja: ", baraja_uno)

baraja_dos = baraja.creaBaraja()
print("Esta es la segunda baraja: ", baraja_dos)
baraja.barajar(baraja_dos)
print("Esta es la segunda baraja desordenada: ", baraja_dos)