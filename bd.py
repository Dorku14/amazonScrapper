import sqlite3

def obtenerRegistrosProductos():
    conexion = sqlite3.connect("bd\productosAmazon.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT url,precioInteres,tienePrioridad,UrlCorta FROM producto order by tienePrioridad desc")
    resultados = cursor.fetchall() 
    productos = [{"url": fila[0], "precioInteres": fila[1],"tienePrioridad":fila[2],"UrlCorta":fila[3]} for fila in resultados]
    conexion.close()

    return productos