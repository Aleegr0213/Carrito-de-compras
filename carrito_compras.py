def Compra(self, opcion, cantidad_compra):
  if (opcion==1):
    if (cantidad_compra > producto1.cantidad):
      pago = pago + (producto1.precio * cantidad_compra)
      producto1.cantidad -= cantidad_compra
    else:
      print("No puede realizar la compra de esa cantidad de productos solo hay ", producto1.cantidad, " disponibles")
      z = False
  
  elif (opcion==2):
    if (cantidad_compra > producto2.cantidad):
      pago = pago + (producto2.precio * cantidad_compra)
      producto2.cantidad -= cantidad_compra
    else:
      print("No puede realizar la compra de esa cantidad de productos solo hay ", producto2.cantidad, " disponibles")
      z = False
  
  elif (opcion==3):
    if (cantidad_compra > producto3.cantidad):
      pago = pago + (producto3.precio * cantidad_compra)
      producto3.cantidad -= cantidad_compra
    else:
      print("No puede realizar la compra de esa cantidad de productos solo hay ", producto3.cantidad, " disponibles")
      z = False
  
  elif (opcion==4):
    if (cantidad_compra > producto4.cantidad):
      pago = pago + (producto4.precio * cantidad_compra)
      producto4.cantidad -= cantidad_compra
    else:
      print("No puede realizar la compra de esa cantidad de productos solo hay ", producto4.cantidad, " disponibles")
      z = False
  
  elif (opcion==5):
    if (cantidad_compra > producto5.cantidad):
      pago = pago + (producto5.precio * cantidad_compra)
      producto5.cantidad -= cantidad_compra
    else:
      print("No puede realizar la compra de esa cantidad de productos solo hay ", producto5.cantidad, " disponibles")
      z = False

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} - Cantidad: {self.cantidad}"
    
producto1 = Producto("Pinzas", 45.50, 5)
producto2 = Producto("Destornillador", 37.00, 5)
producto3 = Producto("Tijeras", 28.50, 5)
producto4 = Producto("Pegamento", 78.50, 5)
producto5 = Producto("Martillo", 100.0, 5)
productos = [producto1, producto2, producto3, producto4, producto5]

x = True
pago = 0
while (x == True):
  print("Bienvenido a la tienda de herramientas ")
  menu = int(input("¿Qué desea  realizar? \n1.Comprar \n2.Salir"))
  y = True
  while(y == True):
    if(menu == 1):
      agregar_carrito = int(input("¿Desea agregar un articulo al carrito de compras? \n1.Si \n2.No"))
      z = True
      while(z == True):
        if(agregar_carrito == 1):
          for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto}")
          opcion = int(input("Ingrese el numero del articulo del menú"))
          cantidad_compra = int(input("Ingrese la cantidad de articulos que quiere comprar"))
          Compra(opcion, cantidad_compra)
          a = int(input("¿Desea finalizar su compra? \n1. Si \n2. No"))
          if(a == 1):
            print("Su total de compra es de $", pago)
            z = False
            y = False
          elif(a == 2):
            continue
          else: "Seleccione una opción valida"
        
        elif(agregar_carrito == 2):
          z = False
          y = False
        
        else:
          print("Seleccione una opción valida")
          z = False
    
    elif(menu == 2):
      y = False
      x = False

    else:
      print("Seleccione una opción valida")
      y = False