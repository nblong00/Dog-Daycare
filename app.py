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
          \r6) EXIT PROGRAM
          ''')
    menu_choice = input("> ")
    while True:
        if menu_choice in ["1", "2", "3", "4", "5", "6"]:
            return menu_choice
        else:
            print('''
                  \rInvalid entry. Enter one of the below numbered options:
                  \r1) Create new Dog & Owner record
                  \r2) Log new Purchase from Owner
                  \r3) Check current Subscriptions
                  \r4) Create new Owner Subscription record
                  \r5) Edit existing Subscription record
                  \r6) EXIT PROGRAM
                  ''')
            menu_choice = input("> ")


    def app(menu_choice):
        if menu_choice == "1":
            pass
        elif menu_choice == "2":
            pass
        elif menu_choice == "3":
            pass
        elif menu_choice == "4":
            pass
        elif menu_choice == "5":
            pass
        elif menu_choice == "6":
            exit()

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    menu_choice = menu()
