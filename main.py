from clases.pokemon import Pokemon

pokedex = []


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingresa un numero entero valido.")


def elegir_pokemon():
    if not pokedex:
        print("No hay Pokemon capturados.")
        return None
    for i, p in enumerate(pokedex, start=1):
        print(f"{i}. {p.nombre} (Nivel {p.nivel})")
    numero = pedir_entero("Elige un numero (0 para cancelar): ")
    if numero < 1 or numero > len(pokedex):
        return None
    return pokedex[numero - 1]


def capturar():
    nombre = input("Nombre: ").strip().title()
    tipo = input("Tipo: ").strip().title()
    ataque = pedir_entero("Ataque: ")
    defensa = pedir_entero("Defensa: ")
    salud = pedir_entero("Salud: ")
    pokedex.append(Pokemon(nombre, tipo, ataque, defensa, salud))


def entrenar():
    pokemon = elegir_pokemon()
    if pokemon is None:
        return
    texto = input("Estadisticas a mejorar (ataque defensa salud), Enter para todas: ")
    pokemon.entrenar(*texto.lower().split())


def ver_info():
    if not pokedex:
        print("No hay Pokemon capturados.")
        return
    for p in pokedex:
        p.mostrar_info()


def contar():
    Pokemon.total_pokemons()


def liberar():
    pokemon = elegir_pokemon()
    if pokemon is None:
        return
    pokedex.remove(pokemon)
    del pokemon


def menu():
    print("\n--- SIMULADOR DE ENTRENAMIENTO POKEMON ---")
    print("1. Capturar nuevo Pokemon")
    print("2. Entrenar un Pokemon")
    print("3. Ver informacion de todos los Pokemon")
    print("4. Calcular cuantos Pokemon existen")
    print("5. Liberar un Pokemon")
    print("0. Salir")


def main():
    acciones = {"1": capturar, "2": entrenar, "3": ver_info, "4": contar, "5": liberar}
    while True:
        menu()
        opcion = input("Opcion: ").strip()
        if opcion == "0":
            break
        if opcion in acciones:
            acciones[opcion]()
        else:
            print("Opcion no valida.")
    pokedex.clear()


if __name__ == "__main__":
    main()
