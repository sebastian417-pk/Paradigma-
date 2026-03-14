temperaturas = [22, 35, 18, 40, 28, 15, 37]

resultado = list(
    map(lambda x: x * 1.5,
        filter(lambda x: x > 30, temperaturas))
)

print(f"Temperaturas ajustadas: {resultado}")