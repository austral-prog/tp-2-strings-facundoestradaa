def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    gasto = (float(input("Ingresar gasto.")))
    dinero_recibido = (float(input("Dinero recibido:")))


    vuelto=dinero_recibido - gasto

    pesos=int(vuelto)
    centavos=round((vuelto-pesos)*100)

    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)


