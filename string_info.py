def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"

    longitud=len(palabra)
    primera= palabra[0]
    ultima= palabra[11]
    repetida= palabra*3
    decorada= "***" + palabra + "***"

    print(f"Palabra: {palabra}")
    print(f"Longitud: {len(palabra)}")
    print(f"Primera letra: {palabra[0]}")
    print(f"Ultima letra: {palabra[11]}")
    print(f"Repetida: {palabra*3}")
    print(f"Decorada: ***{palabra}***")


