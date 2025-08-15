class Producto: 
    
    # Constructor, a diferencia de en java, se les pone un nombre especial y usan # self para referirse a la instancia del objeto (como "this" en java). Ademas, definen las funciones con "def"
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    # Entonces con eso literal ya esta creada la clase, no hace falta decir tipo de dato, ni crear un metodo para el constructor, todo se hace ahi guatafac
    # Ahora si, arrancamos con los metodos, primero el mostrar atributos
    def mostrar_atributos(self):
        print(f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")

# Ejemplo de uso de la clase Producto
# A TENER EN CUENTA: Aca las declaraciones se manejan directamente con la sangria, si yo le meto un tab a esta declaracion de producto 1, ya me lo toma como que es parte de la clase Producto, y no como una instancia de la misma.        
producto1 = Producto("Laptop", 300, 1)
producto1.mostrar_atributos()  # Igualito que en java ponele