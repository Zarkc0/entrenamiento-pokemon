class Pokemon:
    total = 0

    def __init__(self, nombre, tipo, ataque, defensa, salud):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        Pokemon.total += 1
        print(f"Se ha creado a {self.nombre} (tipo {self.tipo}).")

    def __del__(self):
        Pokemon.total -= 1
        print(f"{self.nombre} ha sido liberado")

    def entrenar(self, *stats):
        mejoras = {"ataque": 3, "defensa": 2, "salud": 10}
        if not stats:
            stats = ("ataque", "defensa", "salud")
        validas = [s for s in stats if s in mejoras]
        if not validas:
            print("No hay estadisticas validas para entrenar.")
            return
        self.nivel += 1
        for stat in validas:
            setattr(self, stat, getattr(self, stat) + mejoras[stat])
        print(f"{self.nombre} subio al nivel {self.nivel} (mejoro: {', '.join(validas)}).")

    def mostrar_info(self):
        print(f"{self.nombre} | Tipo: {self.tipo} | Nivel: {self.nivel} | "
              f"Ataque: {self.ataque} | Defensa: {self.defensa} | Salud: {self.salud} | "
              f"Poder total: {self.poder_total()}")

    def poder_total(self):
        return self.ataque + self.defensa + self.salud

    def atacar(self, objetivo):
        danio = max(1, self.ataque - objetivo.defensa)
        objetivo.salud = max(0, objetivo.salud - danio)
        print(f"{self.nombre} ataco a {objetivo.nombre} y le quito {danio} de salud. "
              f"Salud restante: {objetivo.salud}")

    @classmethod
    def total_pokemons(cls):
        """Muestra cuántos Pokémon han sido creados."""
        print(f"Pokemon existentes: {cls.total}")
        return cls.total
