from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql 

from flask import g 
#from pymysql import *  

#engine = create_engine("mysql://root:root@localhost/world", echo=True, convert_unicode=True)
#db_session = scoped_session(sessionmaker(autocommit=False , autoflush = False , bind=engine))
#Base = declarative_base()
#Base.query = db_session.query_property()

#def init_db():
#    #import models
    #Base.metadata.create_all(bind=engine)

#configuration 
#_HOST = "localhost"
#_USER = "root"
#_PASSWORD = "root"
#_DB = "world" 
#_CHARSET = "utf8" 

#def connect_db() : 
#    return pymysql.connect(host='localhost' , user='root', password='root', db='world', charset='utf8') 

#def query_db(query, args=(), one=False):
#    cur = g.db.execute(query, args)
#    rv = [dict((cur.discrio
    

    

    
