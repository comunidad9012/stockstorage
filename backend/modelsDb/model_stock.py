from modelsDb import conexion
from sqlalchemy import Column, Integer, String

class Stock(conexion.Base):
     
     __table_name__='stock'

     idProducto=Column(Integer, autoincrement=True, primary_key=True)
     nombreProducto=Column(String,nullable=False)
     cantidad=Column(Integer,nullable=False)
     costo=Column(Integer,nullable=False)
     venta=Column(Integer,nullable=False)
     idProveedor=Column(Integer)#clave foranea del proveedor
     categoria=Column(Integer)#clave foranea de la categoria

     def __init__(self,idProducto,nombreProducto,cantidad,costo,venta,idProveedor,idCategoria):
         self.idProducto=idProducto
         self.nombreProducto=nombreProducto
         self.cantidad=cantidad
         self.costo=costo
         self.venta=venta
         self.idProveedor=idProveedor
         self.idCategoria=idCategoria