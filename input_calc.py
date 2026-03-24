def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base=(int(input("Base:")))
    altura=(int(input("Altura: ")))

    area_resultado=base*altura
    perimetro= ((base+altura)*2)

    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Area: {area_resultado}")
    print(f"Perimetro: {perimetro}") 
