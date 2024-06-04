"""
Una clase
"""
import time
import datetime

class elcoso:
    """ Es cualquier cosa.
    Haremos algo y devoleremos algún resultado.
    """
    
    def __init__(selt) -> None:
        """Constructor.
        Pues eso.
        """
        self.fecha_creacion = int(time.time())
        self.year_creacion = datetime.datetime.fromtimestamp(self.fecha_creacion).strftime('%Y')

    def fecha_creacion(self) -> int:
        return self.fecha_creacion

    def print_fecha_creacion(self):
        formatted_time = datetime.datetime.fromtimestamp(self.fecha_creacion).strftime('%Y-%m-%d %H:%M:%S')
        print(formatted_time)
