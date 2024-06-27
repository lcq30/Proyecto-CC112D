def invertir_cadena(cadena):
    invertida = ""
    for caracter in cadena:
        invertida = caracter + invertida
    return invertida
cadena1 = "Apruebeme profe"
cadena2 = invertir_cadena(cadena1)
print(cadena2)