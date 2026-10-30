# Pruebas unitarias del caso CP-02: cálculo del MAD (Desviación Media Absoluta)
import pytest

from reportes import calcular_mad


def test_mad_con_tres_datos_da_8_33():
    # Arrange: errores absolutos 10, 5 y 10 -> promedio 25 / 3
    reales = [100, 120, 90]
    pronosticos = [110, 115, 100]

    # Act
    resultado = calcular_mad(reales, pronosticos)

    # Assert: se usa tolerancia porque es un número decimal
    assert resultado == pytest.approx(8.3333, abs=0.01)


def test_mad_cuando_pronostico_es_perfecto_da_cero():
    # Arrange: el pronóstico coincide exactamente con lo real
    reales = [100, 120, 90]
    pronosticos = [100, 120, 90]

    # Act
    resultado = calcular_mad(reales, pronosticos)

    # Assert
    assert resultado == pytest.approx(0)


def test_mad_con_listas_de_distinto_tamano_lanza_error():
    # Arrange: falta un pronóstico, no se pueden comparar
    reales = [100, 120, 90]
    pronosticos = [110, 115]

    # Act y Assert
    with pytest.raises(ValueError):
        calcular_mad(reales, pronosticos)


def test_mad_con_listas_vacias_lanza_error():
    # Arrange: sin datos no hay promedio posible
    reales = []
    pronosticos = []

    # Act y Assert
    with pytest.raises(ValueError):
        calcular_mad(reales, pronosticos)
