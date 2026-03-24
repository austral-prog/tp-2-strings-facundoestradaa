
def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre=input()
    appelido= input()
    minuscula= nombre.lower() + " " + appelido.lower()
    titulo= nombre.title() + " " + appelido.title()
    mayuscula= nombre.upper() + " " + appelido.upper()
    medio= "\t" + nombre.lower() + " " + appelido.lower()

    print(minuscula)
    print(titulo)
    print(mayuscula)
    print(medio)
