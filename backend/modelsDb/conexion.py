from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#conexion con SQLALCHEMY
host="localhost" #lo cambie por el nombre del servicio mysql de docker
user="usuario"
password="root"
db="stockstorage"

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:3306/{db}')
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()