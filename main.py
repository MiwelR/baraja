import barajaC

palos = [' de Oros', ' de Copas', ' de Espadas', ' de Bastos']
numeros = ['A', '1', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']

miBaraja = barajaC.Baraja(palos, numeros)

print("Mi baraja ordenada: ", miBaraja.mazacote)

miBaraja.barajar()

numerojugadores = int(input("¿Cuántos jugadores van a jugar?: "))
numerocartas = int(input("¿Cuántas cartas se repartirán a cada jugador?: "))
print(miBaraja.repartir(numerojugadores, numerocartas))

#print("Mi baraja desordenada: ", miBaraja.mazacote)