# Importación del módulo que permite generar números aleatorios.
import random

# Representación de una línea de metro: '1' indica estación, '0' indica tramos sin estación.
L = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]

# Definición de los trenes y sus atributos:
# posición, dirección (1 es derecha, -1 es izquierda), lista de pasajeros y si está en una estación.
M = [[0, 1, [], True], [16, 1, [], False],[24, 1, [], False],[24, -1, [], False], [32, 1, [], False], [16, -1, [], False], [32, -1, [], False], [47, -1, [], True]]

C = [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# Inicialización del diccionario que mantiene un registro de los pasajeros en cada estación.
E = {i: [] for i in range(len(L)) if L[i] == 1}

# Lista que recopilará el tiempo que cada pasajero pasa en el metro.
T = []

# Comienza una simulación que durará 600 "minutos" o ciclos.
for t in range(1, 961):     
    # Genera pasajeros para cada estación.
    for e in E:
        for _ in range(random.randint(0,20)):
            # Elige un destino al azar para el pasajero.
            d = random.choice(list(E.keys()))
            # Asegura que el destino no sea la misma estación donde se encuentra.
            while d == e:
                d = random.choice(list(E.keys()))
            # Añade el pasajero y su destino al registro de la estación.
            E[e].append((d,t))
            print(E)

    # Gestiona la lógica de movimiento y acción de cada tren.
    for m in M:
        # Si el tren está en una estación:
		print(M)
        if m[-1]:
            # Descarga los pasajeros que han llegado a su destino y registra cuánto tiempo estuvieron en el tren.
            for i in range(len(m[2])-1, -1, -1):
                if m[2][i][0] == m[0]:
                    T.append(t-m[2][i][1])
                    m[2].pop(i)
            # Carga a los pasajeros que van en la dirección del tren.
            i = 0
            while i < len(E[m[0]]):
                if ((E[m[0]][i][0] - m[0]) * m[1]) > 0:
                    m[2].append(E[m[0]][i])
                    E[m[0]].pop(i)
                else:
                    i += 1
            # Marca el tren como que no está en una estación después de cargar/descargar pasajeros.
            m[-1] = False
        # Si el tren no está en una estación:
        else:
            # Mueve el tren en su dirección.
            m[0] += m[1]
            # Si el tren llega al inicio o al final, invierte su dirección.
            if m[0] in [0, len(L)-1]:
                m[1] *= -1
            # Si el tren llega a una estación, lo marca como tal.
            if L[m[0]] == 1:
                m[-1] = True

    # Imprime el estado actual de la simulación para que el usuario pueda seguirlo.
    print("\n----------------------------")
    print(f"Tiempo: {t}")
    print("\nMetros:")
    for m in M:
        d = 'derecha' if m[1] == 1 else 'izquierda'
        print(f"\tMetro en posición {m[0]} avanza hacia {d} con {len(m[2])} pasajeros")
    print("\nEstaciones:")
    for e in E:
        print(f"\tEstación en posición {e} tiene {len(E[e])} esperando en el andén")

    # Pausa la simulación, esperando una entrada del usuario para continuar.
    input()

# Una vez finalizada la simulación, calcula e imprime el tiempo medio de viaje de los pasajeros.
print(f"\nEl tiempo medio de viaje fue {sum(T)/len(T):0.1f} minutos")
 