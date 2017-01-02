from sqlalchemy import Column, Integer, String 
from App.database import Base 

class Example(Base):
    __tablename__ = 'tt_example'

    exampleNo = Column(Integer, primary_key = True) 
    exampleTitle = Column(String(1000))
    exampleType = Column(String(5))

    def __init__(self, exampleTitle = None, exampleType = None) :
        self.exampleTitle = exampleTitle 
        self.exampleType = exampleType 


    def __repr__(self):
        return '<Example %r>' % (self.exampleTitle, ) 
