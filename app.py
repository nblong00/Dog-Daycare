from models import (Base, engine, session,
                    Dog, Human, Purchase, Subscription)
import time
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


def check_if_owner_phone_exists(member_phone):
    phone_exists = session.query(Human).filter(Human.phone == member_phone).first()
    while True:
        if phone_exists != None:
            tier = input("Enter tier of subscription (1-3): ")
            new_sub = Subscription(member_id=phone_exists.id, tier=tier, status="Active")
            session.add(new_sub)
            session.commit()
            time.sleep(0.5)
            print("\nNew Subscription added to database!")
            print("------------------------------------")
            print("Would you like to add another subscription? (yes/no)")
            user_input = input("\n> ")
            break
        if phone_exists == None:
            print("\nNumber entered is not in system...")
            print("Choose option below (1-2):")
            print(f"""
                  \r1) Try inputting phone again
                  \r2) Go back to Main Menu
                  """)
            user_input = input("> ")
            if user_input == '1':
                member_phone = input("Enter owner's phone number: ")
            if user_input == '2':
                return True


def check_if_dog_and_owner_exist_for_sub():
    (dog_name, dog_breed,
    owner_name, owner_phone) = dog.dog_info()
    animal_check = session.query(Dog).filter(Dog.name == dog_name).filter(Dog.breed == dog_breed).first()
    phone_check = session.query(Human).filter(Human.phone == owner_phone).first()
    if animal_check == None:
        print("Dog does not currently exist in system.")
        input("Press ENTER add Dog to system...")
        dog.create_dog_owner(dog_name, dog_breed,
                            owner_name, owner_phone)
    elif phone_check != None:
        print("Phone number already exists in system.")
        input("Press ENTER to setup subscription...")
        tier = input("Enter tier of subscription (1-3): ")
        new_sub = Subscription(member_id=phone_check.id, tier=tier, status="Active")
        session.add(new_sub)
        session.commit()
        time.sleep(0.5)
        print("\nNew Subscription added to database!")
        print("------------------------------------")
        print("Would you like to add another subscription? (yes/no)")
        user_input = input("\n> ")
        if user_input in ["yes", "ye", "y"]:
            return False
        elif user_input in ["no", "n"]:
            return True
    elif phone_check == None and animal_check != None:
        new_owner = Human(dog_id=animal_check.id, name=owner_name, phone=owner_phone)
        session.add(new_owner)
        session.commit()
        print("\nNew Owner added to database!")
        print("------------------------------------")
        input("Press ENTER to start subscription setup...")
        phone_exists = session.query(Human).filter(Human.phone == owner_phone).first()
        tier = input("Enter tier of subscription (1-3): ")
        new_sub = Subscription(member_id=phone_exists.id, tier=tier, status="Active")
        session.add(new_sub)
        session.commit()
        time.sleep(0.5)
        print("\nNew Subscription added to database!")
        print("------------------------------------")
        print("Would you like to add another subscription? (yes/no)")
        user_input = input("\n> ")
        if user_input in ["yes", "ye", "y"]:
            return False
        elif user_input in ["no", "n"]:
            return True


def create_owner_sub():
    exit_to_menu = 0
    while not exit_to_menu:
        print("\nIs Owner registered in system? (yes/no)")
        print("* Enter EXIT to return to Main Menu.")
        owner_exist = input("\n> ")
        if owner_exist in ["yes", "ye", "y"]:
            member_phone = input("Enter owner's phone number: ")
            exit_to_menu = check_if_owner_phone_exists(member_phone)
        if owner_exist in ["no", "n"]:
            print("Is Dog registered in system? (yes/no)")
            print("* Enter EXIT to return to Main Menu.")
            missing_item = input("\n> ")
            if missing_item in ["yes", "ye", "y"]:
                exit_to_menu = check_if_dog_and_owner_exist_for_sub()
            elif missing_item in ["no", "n"]:
                input("\nPress ENTER add Dog to system...")
                (dog_name, dog_breed,
                 owner_name, owner_phone) = dog.dog_info()
                dog.create_dog_owner(dog_name, dog_breed,
                                 owner_name, owner_phone)
            elif missing_item.lower() == "exit":
                break
        elif owner_exist.lower() == "exit":
            break


def check_current_subs():
    current_subs = session.query(Subscription).all()
    print("\nFetching current subscribers...")
    time.sleep(1)
    print("----------------------------------------")
    for sub in current_subs:
        sub_user = session.query(Human).filter(Human.id == sub.member_id).first()
        print(f"Sub_ID: {sub.id} | Name: {sub_user.name} | Phone: {sub_user.phone} | Tier: {sub.tier} | Status: {sub.status}")
    print("----------------------------------------")
    input("\nPress ENTER to return back to Main Menu...")


def sub_menu_decision_tree(menu_decision, subscription):
    if menu_decision == "1":
        subscription.status = "Active"
        return True
    elif menu_decision == "2":
        subscription.status = "Deactivated"
        return True
    elif menu_decision == "3":
        while True:
            try:
                tier_change = input("Enter tier to change to (1-3): ")
                if tier_change in ["1", "2", "3"]:
                    subscription.tier = int(tier_change)
                    return True
                else:
                    raise ValueError
            except ValueError:
                print("\nEntry needs to be either 1, 2, or 3")
                input("Press ENTER to try entering current tier again...\n")
    elif menu_decision == "4":
        return False
    elif menu_decision == "5":
        return 'main-menu'


def subscriber_status_change_menu():
    sub_menu_exit_choice = 0
    while not sub_menu_exit_choice:
        phone_number = input("Enter subscriber's phone number: ")
        subscriber = session.query(Human).filter(Human.phone == phone_number).first()
        time.sleep(0.5)
        print("\n----------------------------------------")
        time.sleep(0.5)
        if subscriber != None:
            print(f"""
                  \rSubscriber selected-
                  \rPhone Number: {phone_number} | Name: {subscriber.name}\n
                  \rSelect one of the below options:
                  \r1) Reactivate subscriber status
                  \r2) Deactivate subscriber status
                  \r3) Change current tier
                  \r4) Back to enter phone number
                  \r5) Go back to Main Menu
                  """)
            menu_decision = input("> ")
            subscription = session.query(Subscription).filter(Subscription.member_id == subscriber.id).first()
            sub_menu_exit_choice = sub_menu_decision_tree(menu_decision, subscription)
            if sub_menu_exit_choice == 'main-menu':
                return 'main-menu'
            elif sub_menu_exit_choice == True:
                return True


def change_status_on_sub():
    end_loop = 0
    while not end_loop:
        end_loop = subscriber_status_change_menu()
        if end_loop == 'main-menu':
            break
        session.commit()
        print("\nSubscription updated!")
        print("------------------------------------")
        print("Would you like to change another subscription? (yes/no)")
        print(end_loop)
        user_input = input("\n> ")
        if user_input in ["yes", "ye", "y"]:
            end_loop = 0


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
            create_owner_sub()
        elif menu_choice == "4":
            check_current_subs()
        elif menu_choice == "5":
            change_status_on_sub()
        elif menu_choice == "6":
            exit()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app()
