class Transaccion:
    def __init__(self, monto:int):
        self.monto = monto
    
    def _validar_monto(self, monto:int) -> bool:
        minimo = 0
        return monto > minimo
    
    def ingresar(self, monto:int):
        if(self._validar_monto(monto)):
            self.monto += monto
    
    def retirar(self, monto:int):
        if(self._validar_monto(monto) and (monto <= self.monto)):
            self.monto -= monto
    
    def transferir(self, monto:int):
        if(self._validar_monto(monto) and (monto <= self.monto)):
            self.monto -= monto
            # Aca falta por desarrollar el enviarle el monto ingresado a otro usuario existente