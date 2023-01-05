#!/usr/bin/env python

# Primero importamos el paquete de logs
import logging

# Creamos un objeto logger para escribir sobre el
LOGGER = logging.getLogger(__name__)

# Añadimos un manejador de flujo, que escribirá en las salidas estandar y error estándar
logger_handler = logging.StreamHandler()
logger_handler.setLevel(logging.DEBUG)
logger_handler.setFormatter(CustomFormatter())
    
LOGGER.addHandler(logger_handler)

# Definimos el nivel por defecto del logger, los valores posibles son: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGGER.setLevel("DEBUG")

# Luego podemos utilizar los métodos de escritura del logger
LOGGER.debug("debug message")
LOGGER.info("info message")
LOGGER.warning("warning message")
LOGGER.error("error message")
LOGGER.critical("critical message")


# Opcional: Usamos un formateador personalizado para darle color a los mensajes
# Tomado de https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
      
logger_handler = logging.StreamHandler()
logger_handler.setLevel(logging.DEBUG)
logger_handler.setFormatter(CustomFormatter())
LOGGER.addHandler(logger_handler)

LOGGER.debug("debug message")
LOGGER.info("info message")
LOGGER.warning("warning message")
LOGGER.error("error message")
LOGGER.critical("critical message")
