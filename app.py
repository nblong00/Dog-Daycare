from models import (Base, engine, session,
                    Dog, Human, Purchase, Subscription)
import time


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
        while True:
            dog_name = input("Enter dog's name: ")
            dog_breed = input("Enter dog's breed: ")
            owner_name = input("Enter owner's name: ")
            owner_phone = input("Enter owner's phone number: ")
            animal_check = session.query(Dog).filter(Dog.name == dog_name).filter(Dog.breed == dog_breed).first()
            if animal_check == None:
                new_dog = Dog(name = dog_name, breed = dog_breed)
                newest_dog = session.query(Dog).order_by(Dog.id.desc()).first()
                new_owner = Human(dog_id = (newest_dog.id + 1), name = owner_name, phone = owner_phone)
                session.add_all([new_dog, new_owner])
                session.commit()
                time.sleep(0.5)
                print('New Dog and Owner added to database!')
                return
            else:
                print("\nDog and breed combo already exists in database.")
                print("Enter info for dog not currently in system.")
                continue
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
    else:
        pass


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    menu_choice = menu()
    app(menu_choice)
