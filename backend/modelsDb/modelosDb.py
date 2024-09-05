import conexion
from sqlalchemy import Column, Integer, String, Float, Date

class Usuario(conexion.Base):
    __tablename__='usuario'

    id= Column(Integer, autoincrement=True, primary_key=True)
    username=Column(String, nullable=False)

    def __init__(self,username):
        self.username=username

class Cliente(conexion.Base):
    __tablename__='cliente'

    idCliente= Column(Integer, autoincrement=True, primary_key=True)
    nombre=Column(String, nullable=False)
    dni= Column(Integer, nullable=False)
    telefono= Column(Integer, nullable=False)

    

    def __init__(self,idCliente,nombre,dni,telefono):
        self.idCliente=idCliente
        self.nombre=nombre
        self.dni=dni
        self.telefono=telefono


class Proveedor(conexion.Base):
    __tablename__='proveedor'

    idProveedor= Column(Integer, autoincrement=True, primary_key=True)
    direccion=Column(String(100),nullable=False)
    empresa=Column(String(100),nullable=False)
    telefono=Column(Integer, nullable=False )

    def __init__(self,direccion,empresa,telefono):
        self.direccion=direccion
        self.empresa=empresa
        self.telefono=telefono

class Categoria(conexion.Base):
    __table_name__='categoria'

    idCategoria=Column(Integer,nullable=False, autoincrement=True)
    categoriaProducto=Column(String(50), nullable=False)

    def __init__(self,categoria):
        self.categoria=categoria

class Factura(conexion.Base):
    __table_name__='factura'

    nroFactura= Column(Integer, autoincrement=True, primary_key=True)
    id_cliente=Column(Integer,nullable=False) #aca va la relacion con cliente
    fecha=Column(Date,nullable=False)
    descripcion=Column(String, nullable=False )
    medioDePago=Column(Integer, nullable=False )
    descuento=Column(Integer,nullable=False)
    total=Column(Integer,nullable=False) 

    def __init__(self,nroFactura,idCLiente,fecha,descripcion,medioDePago,descuento,total):
        self.nroFactura=nroFactura
        self.id_cliente=idCLiente
        self.fecha=fecha
        self.descripcion=descripcion
        self.medioDePago=medioDePago
        self.descuento=descuento
        self.total=total
    

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


class DetalleFactura(conexion.Base):
    __table_name__='detalleFactura'

    idDetalle= Column(Integer, autoincrement=True, primary_key=True)
    cantidad=Column(Integer, nullable=False )
    total=Column(Integer, nullable=False )
    facturaID= Column(Integer)#clave foranea con factura
    idProductos= Column(Integer)#clave foranea productos
    
    def __init__(self,idDetalle,cantidad,total,facturaId,idProductos):
        self.idDetalle=idDetalle
        self.cantidad=cantidad
        self.facturaID=facturaId
        self.idProductos=idProductos
        self.total=total