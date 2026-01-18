"""Ejemplo de variables y tipos básicos"""

def demo():
    entero = 10
    flotante = 3.14
    texto = "texto de ejemplo"
    booleano = True
    lista = [1, 2, 3]

    print(f"entero={entero} tipo={type(entero)}")
    print(f"flotante={flotante} tipo={type(flotante)}")
    print(f"texto='{texto}' tipo={type(texto)}")
    print(f"booleano={booleano} tipo={type(booleano)}")
    print(f"lista={lista} tipo={type(lista)}")


if __name__ == "__main__":
    demo()
