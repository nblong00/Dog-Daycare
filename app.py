from models import (Base, engine, session,
                    Dog, Human, Purchase, Subscription)

if __name__ == "__main__":
    Base.metadata.create_all(engine)