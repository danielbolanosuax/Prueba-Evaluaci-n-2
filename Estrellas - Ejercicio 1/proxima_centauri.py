class ProximaCentauri:
    def __init__(self):
        self.nombre = "Proxima Centauri"
        self.tipo = "Estrella enana roja"
        self.constelacion = "Centaurus"
    
    def info(self):
        return f"{self.nombre}, una {self.tipo} en la constelación {self.constelacion}."
