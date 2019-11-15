#!/usr/bin/env python

# Primero importamos el paquete de logs
import logging

# Creamos un objeto logger para escribir sobre el
LOGGER = logging.getLogger(__name__)

# Añadimos un manejador de flujo, que escribirá en las salidas estandar y error estándar
LOGGER.addHandler(logging.StreamHandler())

# Definimos el nivel por defecto del logger, los valores posibles son: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGGER.setLevel("DEBUG")

# Luego podemos utilizar los métodos de escritura del logger
LOGGER.debug("debug message")
LOGGER.info("info message")
LOGGER.warning("warning message")
LOGGER.error("error message")
LOGGER.critical("critical message")
