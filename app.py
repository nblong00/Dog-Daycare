from models import (Base, engine, session,
                    Dog, Human, Purchase, Subscription)


def menu():
    print('''
          \n-Dog Daycare Admin Program-
          \rChoose one of the below options:
          \r1) Create new Dog & Owner record
          \r2) Log new Purchase from Owner
          \r3) Check current Subscriptions
          \r4) Create new Owner Subscription record
          \r5) Edit existing Subscription record
          ''')
    menu_choice = input("\n> ")
    while True:
        if menu_choice in ["1", "2", "3", "4", "5"]:
            return menu_choice
        else:
            print('''
                  \rInvalid entry. Enter one of the below numbered options:
                  \r1) Create new Dog & Owner record
                  \r2) Log new Purchase from Owner
                  \r3) Check current Subscriptions
                  \r4) Create new Owner Subscription record
                  \r5) Edit existing Subscription record
                  ''')
            menu_choice = input("\n> ")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    menu()
