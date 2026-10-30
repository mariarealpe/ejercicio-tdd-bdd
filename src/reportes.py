def calcular_mad(reales, pronosticos):
    if len(reales) != len(pronosticos):
        raise ValueError("Las listas deben tener el mismo tamaño")
    if len(reales) == 0:
        raise ValueError("Las listas no pueden estar vacías")
    suma = 0
    for i in range(len(reales)):
        suma = suma + abs(reales[i] - pronosticos[i])
    return suma / len(reales)
