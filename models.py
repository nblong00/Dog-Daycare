from sqlalchemy import (create_engine, Column,
                        Integer, ForeignKey, String)
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine('sqlite:///daycare.db', echo = False)
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()


class Dog(Base):
    __tablename__= 'Dogs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)
    owner = relationship('Human', back_populates = 'dog')

    def __repr__(self):
        return f'<Dog ID: {self.id}, Name: {self.name}, Breed: {self.breed}>'


class Human(Base):
    __tablename__ = 'Owner'
    id = Column(Integer, primary_key=True)
    dog_id = Column(Integer, ForeignKey('Dogs.id'))
    name = Column(String)
    phone = Column (String)
    dog = relationship('Dog', back_populates = 'owner')

    def __repr__(self):
        return f'<Owner ID: {self.id}, Name: {self.name}, Dog ID: {self.dog_id}, Phone: {self.phone}>'


if __name__ == '__main__':
    Base.metadata.create_all(engine)