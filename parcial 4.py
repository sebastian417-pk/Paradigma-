def contar_palabras(texto):
    conteo = {}
    for palabra in texto.split():
        if palabra not in conteo:
            conteo[palabra] = 0
        conteo[palabra] += 1
    return conteo


frase = "el gato y el perro y el pez"
resultado = contar_palabras(frase)
print(resultado)