def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """

    frase = (input("Frase: ").lower())
    print(f"Contiene a: {"a" in frase}")
    print(f"Contiene e: {"e" in frase}")
    print(f"Contiene i: {"i" in frase}")
    print(f"Contiene o: {"o" in frase}")
    print(f"Contiene u: {"u" in frase}")

