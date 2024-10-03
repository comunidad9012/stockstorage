from modelsDb import conexion
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin

class Usuario(conexion.Base, UserMixin):
    __tablename__='usuarios'

    id = Column(Integer, autoincrement=True, primary_key=True)
    email=Column(String(100), nullable=False)
    password=Column(String(100), nullable=False)

    def __init__(self,email,password):
        self.email=email
        self.password=password
