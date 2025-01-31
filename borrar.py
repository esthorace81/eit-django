class CortaCadena:
    def __init__(self, nombre) -> None:
        self.cadena = nombre

    def __truediv__(self, numero):
        return self.cadena[0:numero]


texto = 'Hola mundo'
cortar = CortaCadena(texto)
print(cortar / 4)
print(cortar / 2)
