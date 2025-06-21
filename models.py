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
        return f'<Dog(ID: {self.id}, Name: {self.name}, Breed: {self.breed})>'


class Human(Base):
    __tablename__ = 'Owner'
    id = Column(Integer, primary_key=True)
    dog_id = Column(Integer, ForeignKey('Dogs.id'))
    name = Column(String)
    phone = Column (String)
    dog = relationship('Dog', back_populates = 'owner')
    purchase = relationship('Purchase', back_populates = 'member')

    def __repr__(self):
        return f'<Owner(ID: {self.id}, Dog ID: {self.dog_id}, Name: {self.name}, Phone: {self.phone})>'


class Purchase(Base):
    __tablename__ = 'Purchases'
    id = Column(Integer, primary_key=True)
    human_id = Column(Integer, ForeignKey('Owner.id'))
    item = Column(String)
    price = Column(Integer)
    member = relationship('Human', back_populates = 'purchase')

    def __repr__(self):
        return f'<Purchase(ID: {self.id}, Member ID: {self.human_id}, Price: {self.price})>'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
