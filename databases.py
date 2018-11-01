from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name, price, quantity, company):
	product_object = Product(
		name = name, 
		price = price,
		quantity = quantity,
		company = company ) 
	session.add(product_object)
	session.commit()
create_product("Iphone", 1200 , 5, "Apple")


def delete_product (name):
	session.query(Product).filter_by(name=name).delete()
	session.commit()


  #TODO: complete the functions (you will need to change the function's inputs)
  
def update_product():
  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def delete_product(id):
  pass

def get_product(id):
  pass
