# Pasos (steps) BDD del caso CP-03: habilitar el botón Exportar
import pytest
from pytest_bdd import given, scenarios, then, when

from exportacion import boton_exportar_habilitado

# Conecta todos los escenarios del archivo .feature con estas pruebas
scenarios("exportar_reportes.feature")


@pytest.fixture
def contexto():
    # Diccionario para pasar datos de un paso al siguiente
    return {}


@given("a dashboard with no products with loaded data")
def dashboard_sin_productos(contexto):
    contexto["productos_con_datos"] = []


@given("a dashboard with 1 product with loaded data")
def dashboard_con_un_producto(contexto):
    contexto["productos_con_datos"] = ["Producto A"]


@when("the user opens the reports screen")
def abrir_pantalla_reportes(contexto):
    # Al abrir la pantalla se decide si el botón queda habilitado
    contexto["boton_habilitado"] = boton_exportar_habilitado(contexto["productos_con_datos"])


@then("the Export button should be disabled")
def boton_deshabilitado(contexto):
    assert contexto["boton_habilitado"] is False


@then("the Export button should be enabled")
def boton_habilitado(contexto):
    assert contexto["boton_habilitado"] is True
