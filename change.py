def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    print("Ingresar gasto:")
    gasto = float(input())
    print(gasto)
    print("Dinero recibido")
    dinero_recibido = int(input())
    print(dinero_recibido)
    vuelto = dinero_recibido - gasto
    vuelto_redondo= vuelto // 1
    print(f"\nVuelto\n")
    print(f"Pesos:\n{int(vuelto_redondo)}")
    centavos = (vuelto - vuelto_redondo) * 100
    print(f"Centavos:\n{int(centavos)}")

