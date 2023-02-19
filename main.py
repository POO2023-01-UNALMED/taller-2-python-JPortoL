class Asiento:
    def __init__(self, color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self,color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color=color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self,registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        if tipo=="electrico" or tipo=="gasolina":
            self.tipo = tipo

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        cantidadCreados = 0
    def cantidadAsientos(self):
        sum=0
        for asiento in self.asientos:
            if asiento != None:
                sum+=1
        return sum
    def verificarIntegridad(self):
        sum=0
        if self.registro==self.motor.registro:
            for asiento in self.asientos:
                if asiento != None and asiento.registro != self.registro:
                    sum+=1
        else:
            sum+=1
        if sum>0:
            return "Las piezas no son originales"
        else:
            return "Auto original"







