from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password_hash = Column(String)

    def setPassword(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verifyPassword(self, hash):
        return pwd_context.verify(hash, self.password_hash)

    @property
    def serialize(self):
	    """Return object data in easily serializeable format"""
	    return {
            'username' : self.username,
            'id' : self.id,
	    }

class Bagel(Base):
	__tablename__ = 'bagel'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	picture = Column(String)
	description = Column(String)
	price = Column(String)
	@property
	def serialize(self):
	    """Return object data in easily serializeable format"""
	    return {
	    'name' : self.name,
	    'picture' : self.picture,
	    'description' : self.description,
	    'price' : self.price
	        }


engine = create_engine('sqlite:///bagelShop.db')


Base.metadata.create_all(engine)
