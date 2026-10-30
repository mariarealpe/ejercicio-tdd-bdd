# Regla de negocio del caso CP-03 para el botón Exportar


def boton_exportar_habilitado(productos_con_datos):
    # Solo tiene sentido exportar si hay al menos un producto con datos
    return len(productos_con_datos) > 0
