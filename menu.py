import sqlite3

conexion=sqlite3.connect("dato_registros.db")
cursor= conexion.cursor()




def menu_productos():
    print('======== SUPERMERCADO EL AHORRO ========')
    print('1. Resgistrar producto')
    print('2. Mostrar productos')
    print('3. Buscar producto')
    print('4. Modificar producto')
    print('5. Eliminar producto')
    print('6. Buscar producto por categoria')
    print('7. Mostrar productos agotados')
    print('8. Calcular el total de productos')
    print('9. Salir')
    

    
def registrar_producto():
    print('======== REGISTRAR PRODUCTO ========')

    nombre = input('Ingrese el nombre del producto: ')
    categoria = input('Ingrese la categoria del producto: ')
    precio_compra = float(input('Ingrese el precio de compra: '))
    precio_venta = float(input('Ingrese el precio de venta: '))
    cantidad_disponible = int(input('Ingrese la cantidad disponible: '))
    proveedor = input('Ingrese el nombre del proveedor: ')

    cursor.execute("""
        INSERT INTO producto (
            nombre,
            Categoria,
            Precio_compra,
            Precio_venta,
            Cantidad_disponible,
            Proveedor
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        nombre,
        categoria,
        precio_compra,
        precio_venta,
        cantidad_disponible,
        proveedor
    ))

    conexion.commit()

    print('-------- Producto registrado exitosamente --------')

    
def mostrar_productos():
    print('======== LISTA DE PRODUCTOS ========')
    cursor.execute("SELECT * FROM producto")
    productos = cursor.fetchall()
    if not productos:
        print('No hay productos')
        return
    for producto in productos:
                
            print('Codigo:',producto[0])
            print('Nombre:',producto[1])
            print('Categoria:',producto[2])
            print('Precio de compra:',producto[3])
            print('Precio de venta:',producto[4])
            print('Cantidad disponible:',producto[5])
            print('Proveedor:',producto[6])
            print('-----------------------------------')
    
    

def buscar_productos():
    print('======== BUSCAR PRODUCTO ========')
    codigo=input('Ingrese el codigo del producto que desea buscar: ')
    cursor.execute(
        "SELECT * FROM producto WHERE id=?",
        (codigo,)
    )
    producto=cursor.fetchall()
    if producto:
        print('Codigo:',producto[0][0])
        print('Nombre:',producto[0][1])
        print('Categoria:',producto[0][2])
        print('Precio de compra:',producto[0][3])
        print('Precio de venta:',producto[0][4])
        print('Cantidad disponible:',producto[0][5])
        print('Proveedor:',producto[0][6])
    else:
        print('No se encontro el producto con el codigo ingresado.')
        
def modificar_producto():
    print('======== MODIFICAR PRODUCTO ========')
    codigo=input('Ingrese el codigo del producto que desea modificar: ')
    cursor.execute(
        "SELECT * FROM producto WHERE id = ?",
        (codigo,)
    )
    
    producto=cursor.fetchone()
    if producto is None:
        print('No se encontro producto')
        return
    
    print('Producto encontrado:', producto[1])
    nuevo_nombre=input('Ingrese el nuevo nombre del producto: ')
    nueva_categoria=input('Ingrese la nueva categoria del producto: ')
    nuevo_precio_compra=float(input('Ingrese el nuevo precio de compra del producto: '))
    nuevo_precio_venta=float(input('Ingrese el nuevo precio de venta del producto: '))
    nueva_cantidad_disponible=int(input('Ingrese la nueva cantidad disponible del producto: '))
    nuevo_proveedor=input('Ingrese el nuevo proveedor del producto: ')
    
    cursor.execute("""
                   UPDATE producto
                   SET nombre=?,
                   Categoria=?,
                   Precio_compra=?,
                   Precio_venta=?,
                   cantidad_disponible=?,
                   Proveedor=?
                   WHERE id=?""",
                   (nuevo_nombre,
                    nueva_categoria,
                    nuevo_precio_compra,
                    nuevo_precio_venta,
                    nueva_cantidad_disponible,
                    nuevo_proveedor,
                    codigo))
    conexion.commit()
    print('-------- Producto modificado exitosamente --------')
    
def eliminar_producto():
    print('======== ELIMINAR PRODUCTO ========')
    codigo=input('Ingrese el codigo del producto que desea eliminar: ').lower()
    for indice, producto in enumerate(productos):
        if producto['codigo'].lower()==codigo:
            productos.pop(indice)
            print('-------- Producto eliminado exitosamente --------')
            return
    print('No se encontro el producto con el codigo ingresado.')
    
def buscar_producto_por_categoria():
    print('======== BUSCAR PRODUCTO POR CATEGORIA ========')
    categoria=input('Ingrese la categoria del producto que desea buscar: ').lower()
    encontrados=False
    for producto in productos:
        if producto['categoria'].lower()==categoria:
            print('Codigo:',producto['codigo'])
            print('Nombre:',producto['nombre'])
            print('Categoria:',producto['categoria'])
            print('Precio de compra:',producto['precio_Compra'])
            print('Precio de venta:',producto['precio_Venta'])
            print('Cantidad disponible:',producto['cantidad_disponible'])
            print('Proveedor:',producto['proveedor'])
            print('-----------------------------------')
            encontrados=True
    if not encontrados:
        print('No se encontraron productos en la categoria ingresada.')
        
def mostrar_productos_agotados():
    print('===== PRODUCTOS AGOTADOS =====')
    agotados = [producto for producto in productos
                if producto['cantidad_disponible'] <= 0]
    if not agotados:
        print('No hay productos agotados.')
        return

    for producto in agotados:
        print('Codigo:', producto['codigo'])
        print('Nombre:', producto['nombre'])
        print('Categoria:', producto['categoria'])
        print('Proveedor:', producto['proveedor'])
        print('-----------------------------------')

def total_productos():
    print('======= TOTAL DEL INVENTARIO =======')
    total = sum(
        producto['precio_Venta'] * producto['cantidad_disponible']
        for producto in productos
    )
    print(f'Valor total: {total}')
    
while True:
    
  menu_productos()
  opcion=input('Seleccione una opcion:')
    
  if opcion =='1':
    registrar_producto()
    
  elif opcion=='2':
      mostrar_productos()
  elif opcion=='3':
      buscar_productos()
  elif opcion=='4':
      modificar_producto()
  elif opcion=='5':
      eliminar_producto()
  elif opcion=='6':
      buscar_producto_por_categoria()
  elif opcion=='7':
      mostrar_productos_agotados()
  elif opcion=='8':
      total_productos()
  elif opcion=='9':
      print('Gracias por estar aqui')
      break
      
conexion.close()

