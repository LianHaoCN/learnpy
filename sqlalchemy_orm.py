#-*-coding=utf-8-*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = Column(String(20), primary_key=True)
	name = Column(String(20))
	books = relationship('Book')

class Book(Base):
	__tablename__= 'book'
	id = Column(String(20), primary_key=True)
	name = Column(String(20))
	user_id = Column(String(20), ForeignKey('user.id'))

engine = create_engine('mysql+mysqlconnector://root:TZTJ-VCeIoCM1CG1dWe3@localhost:3306/test')
DBSession = sessionmaker(bind=engine)

#session = DBSession()
#new_user = User(id='5', name='Bob')
#session.add(new_user)
#session.commit()
#session.close()

#session = DBSession()
#new_book = Book(id='1', name='hello', user_id='5')
#new_book1 = Book(id='2', name='world', user_id='5')
#session.add(new_book)
#session.add(new_book1)
#session.commit()
#session.close()

session1 = DBSession()
user = session1.query(User).filter(User.id=='5').one()
print 'type:', type(user)
print 'name:', user.name
print 'book:', user.books
session1.close()
