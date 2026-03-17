def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio=(int(input("Precio:")))
    descuento=(float(input("Descuento:")))
    cantidad = int(input("Cantidad:"))

    precio_con_descuento= precio -descuento


    total = precio_con_descuento*cantidad

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Cantidad:{cantidad}")
    print(f"Precio_con_descuento: {precio_con_descuento}")
    print(f"Total: {total}")
casting()


