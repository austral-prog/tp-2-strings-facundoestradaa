def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """

    nombre = input()
    apellido = input()
    nombre_minuscula = nombre.lower() + " " + apellido.lower()
    nombre_iniciales = nombre.title() + " " + apellido.title()
    nombre_mayuscula = nombre.upper() + " " + apellido.upper()
    print(nombre_minuscula)
    print(nombre_iniciales)
    print(nombre_mayuscula)
    print(f"\t{nombre_minuscula}")






