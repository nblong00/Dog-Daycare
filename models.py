from sqlalchemy import (create_engine, Column,
                        Integer, ForeignKey, String)
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine("sqlite:///daycare.db", echo = False)
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()


class Dog(Base):
    __tablename__= "Dogs"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)
    owner = relationship("Human", back_populates = "dog")

    def __repr__(self):
        return f"<Dog(ID: {self.id}, Name: {self.name}, Breed: {self.breed})>"


class Human(Base):
    __tablename__ = "Owner"
    id = Column(Integer, primary_key=True)
    dog_id = Column(Integer, ForeignKey("Dogs.id"))
    name = Column(String)
    phone = Column (String)
    dog = relationship("Dog", back_populates = "owner")
    purchase = relationship("Purchase", back_populates = "person")
    subscription = relationship("Subscription", back_populates = "member")

    def __repr__(self):
        return f"<Owner(ID: {self.id}, Dog ID: {self.dog_id}, Name: {self.name}, Phone: {self.phone})>"


class Purchase(Base):
    __tablename__ = "Purchases"
    id = Column(Integer, primary_key=True)
    human_id = Column(Integer, ForeignKey("Owner.id"))
    item = Column(String)
    price = Column(Integer)
    person = relationship("Human", back_populates = "purchase")

    def __repr__(self):
        return f"<Purchase(ID: {self.id}, Person ID: {self.human_id}, Price: {self.price})>"


class Subscription(Base):
    __tablename__ = "Subscriptions"
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey("Owner.id"))
    tier = Column(Integer)
    status = Column(String)
    member = relationship("Human", back_populates = "subscription")

    def __repr__(self):
        return f"<Subscription(ID: {self.id}, Member ID: {self.member_id}, Tier: {self.tier}, Status: {self.status})>"
