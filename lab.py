# pylint: disable=redefined-outer-name
import os #funciones para interactuar con el sistema operativo, como limpiar la pantalla.
import readchar #que se utiliza para leer caracteres individuales del teclado sin necesidad de presionar la tecla Enter.

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear') #funcion para limpiar la pantalla de consola

def print_map(mapa):
    limpiar_pantalla()
    for row in mapa:
        print("".join(row))

def main_loop(mapa, inicio, final):
    px, py = inicio

    while (px, py) != final:
        mapa[py][px] = 'P'
        print_map(mapa)

        tecla = readchar.readkey()

        dx, dy = 0, 0

        if tecla == '\x1b[A':  # Flecha arriba
            dy = -1
        elif tecla == '\x1b[B':  # Flecha abajo
            dy = 1
        elif tecla == '\x1b[D':  # Flecha izquierda
            dx = -1
        elif tecla == '\x1b[C':  # Flecha derecha
            dx = 1

        new_px, new_py = px + dx, py + dy #Calcula las nuevas coordenadas del personaje 

        if 0 <= new_px < len(mapa[0]) and 0 <= new_py < len(mapa) and mapa[new_py][new_px] != '#':
            mapa[py][px] = '.'
            px, py = new_px, new_py

def create_map(map_str, inicio, final):
    mapa = [list(row) for row in map_str.split("\n")]
    mapa[inicio[1]][inicio[0]] = '.'
    mapa[final[1]][final[0]] = '.'
    return mapa

if __name__ == "__main__":
    map_str = "..#############\n" \
              "........#.#.#.#\n" \
              "###.###.#.#.#.#\n" \
              "#.#...#.#.....#\n" \
              "#.#.#####.#.#.#\n" \
              "#.....#...#.#.#\n" \
              "#.#.###.#.###.#\n" \
              "#.#.#...#.#...#\n" \
              "###.#.#######.#\n" \
              "#.#...#...#...#\n" \
              "#.###.#.#.#.###\n" \
              "#.#.....#.#...#\n" \
              "#.#.#########.#\n" \
              "#.........#...#\n" \
              "#############.#\n"

    inicio = (0, 0)
    final = (14, 14)

    mapa = create_map(map_str, inicio, final)
    main_loop(mapa, inicio, final)
