from models import (Base, engine)
import subscription
import dog
import purchase


def menu():
    menu =  '''
            \r-Dog Daycare Admin Program-
            \rChoose one of the below options:
            \r1) Create new Dog & Owner record
            \r2) Log new Purchase from Owner
            \r3) Create new Owner Subscription record
            \r4) Check current Subscriptions
            \r5) Edit existing Subscription record
            \r6) EXIT PROGRAM
            '''
    print(menu)
    menu_choice = input("> ")
    while True:
        if menu_choice in ["1", "2", "3", "4", "5", "6"]:
            return menu_choice
        else:
            print("Invalid Entry. Input needs to be a number 1 through 6.\n")
            menu_choice = input("> ")


def app():
    while True:
        menu_choice = menu()
        if menu_choice == "1":
            (dog_name, dog_breed,
            owner_name, owner_phone) = dog.dog_info()
            dog.create_dog_owner(dog_name, dog_breed,
                             owner_name, owner_phone)
        elif menu_choice == "2":
            purchase.log_purchase()
        elif menu_choice == "3":
            subscription.create_owner_sub()
        elif menu_choice == "4":
            subscription.check_current_subs()
        elif menu_choice == "5":
            subscription.change_status_on_sub()
        elif menu_choice == "6":
            exit()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app()
