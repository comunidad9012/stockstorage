from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#conexion con SQLALCHEMY
host="database" #lo cambie por el nombre del servicio mysql de docker
user="usuario"
password="root"
db="stockcommerce"

Base=declarative_base()
#engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{3306}/{db}')
engine= create_engine('mysql+pymysql://usuario:root@database:3306/stockcommerce')
Session=sessionmaker(bind=engine)
session=Session()