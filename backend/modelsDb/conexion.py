from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
engine= create_engine('mysql+pymysql://usuario:root@database:3306/stockcommerce')
Session=sessionmaker(bind=engine)
session=Session()