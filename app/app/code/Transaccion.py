from abc import ABC, abstractmethod

class I_Transaccion(ABC):
    
    @abstractmethod
    def ingresar(self, monto:int):
        pass
    
    @abstractmethod
    def retirar(self, monto:int):
        pass
    
    @abstractmethod
    def transferir(self, monto:int):
        pass

class Usuario:
    def __init__(self, nombre:str, dni:int, email:str, password:str):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.password = password
    
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre:str):
        self.nombre = nombre

    def getDNI(self):
        return self.dni
    def setDNI(self,dni:int):
        self.dni = dni

    def getEmail(self):
        return self.email
    def setEmail(self,email:str):
        self.email = email
    
    def getPassword(self):
        return self.password
    def setPassword(self, password:str):
        self.password = password

class Cuenta(Usuario,I_Transaccion):
    def __init__(self, nombre, dni, email, password, montoInicial):
        super().__init__(nombre, dni, email, password)
        self.monto = montoInicial
    
    def getMonto(self):
        return self.monto
    def setMonto(self,montoIngresado):
        self.monto = montoIngresado
    
    def ingresar(self, monto:int):
        if monto > 0:
            self.monto += monto

    def retirar(self, monto:int):
        if monto > 0 and monto <= self.monto:
            self.monto -= monto

    def transferir(self, monto:int):
        # Desarrollar a futuro
        pass