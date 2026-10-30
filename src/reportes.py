# Cálculo de indicadores de error para el dashboard de reportes


def _validar_listas(reales, pronosticos):
    # Sin la misma cantidad de datos no se puede comparar real contra pronóstico
    if len(reales) != len(pronosticos):
        raise ValueError("Las listas deben tener el mismo tamaño")
    # Sin datos no se puede dividir para sacar el promedio
    if len(reales) == 0:
        raise ValueError("Las listas no pueden estar vacías")


def calcular_mad(reales, pronosticos):
    """Devuelve el MAD: el promedio de los errores absolutos |real - pronóstico|."""
    _validar_listas(reales, pronosticos)
    errores = [abs(real - pronostico) for real, pronostico in zip(reales, pronosticos)]
    return sum(errores) / len(errores)
