class AlphaCentauri:
    def __init__(self):
        self.nombre = "Alpha Centauri"
        self.tipo = "Sistema estelar triple"
        self.constelacion = "Centaurus"
    
    def info(self):
        return f"{self.nombre}, un {self.tipo} en la constelación {self.constelacion}."
