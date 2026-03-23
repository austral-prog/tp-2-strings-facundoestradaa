def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base= int(input())
    altura= int(input())

    print(f"Base: {base}")
    print(f"Altura: {altura}")

    
    area_resultado = base * altura
    perimetro_resultado= (base * 2) + (altura * 2)

    print(f"Area: {area_resultado}")
    print(f"Perimetro: {perimetro_resultado}")



