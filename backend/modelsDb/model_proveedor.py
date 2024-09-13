from modelsDb import conexion
from sqlalchemy import Column, Integer, String

class Proveedor(conexion.Base):
    __tablename__='proveedores'

    idProveedor= Column(Integer, autoincrement=True, primary_key=True)
    direccion=Column(String(100),nullable=False)
    empresa=Column(String(100),nullable=False)
    telefono=Column(Integer, nullable=False )

    def __init__(self,direccion,empresa,telefono):
        self.direccion=direccion
        self.empresa=empresa
        self.telefono=telefono