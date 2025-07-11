from models import (Base, engine, session,
                    Dog, Human, Purchase, Subscription)
import time


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


def dog_info():
    dog_name = input("Enter dog's name: ")
    dog_breed = input("Enter dog's breed: ")
    owner_name = input("Enter owner's name: ")
    owner_phone = input("Enter owner's phone number: ")
    return dog_name, dog_breed, owner_name, owner_phone


def create_dog_owner(dog_name, dog_breed,
                    owner_name, owner_phone):
    while True:
        animal_check = session.query(Dog).filter(Dog.name == dog_name).filter(Dog.breed == dog_breed).first()
        if animal_check == None:
            new_dog = Dog(name=dog_name, breed=dog_breed)
            newest_dog = session.query(Dog).order_by(Dog.id.desc()).first()
            new_owner = Human(dog_id=(newest_dog.id + 1), name=owner_name, phone=owner_phone)
            time.sleep(0.5)
            session.add_all([new_dog, new_owner])
            session.commit()
            print("\nNew Dog and Owner added to database!")
            print("------------------------------------")
            input("Press ENTER to return to Main Menu...")
            break
        else:
            print("\nDog and breed combo already exists in database.")
            print("Enter info for dog not currently in system.\n")
            (dog_name, dog_breed,
            owner_name, owner_phone) = dog_info()
            continue


def purchase_convert():
    purchase = float(input("Enter purchase total (ex. 19.99): "))
    purchase_pennies = int(purchase * 100)
    return purchase_pennies


def log_purchase():
    while True:
        item_name = input("Enter name of item:")
        purchase_pennies = purchase_convert()
        owner_number = input("Enter owner phone number: ")
        owner_record = session.query(Human).filter(Human.phone == owner_number).first()
        purchase = Purchase(human_id=owner_record.id, item=item_name, price=purchase_pennies)
        session.add(purchase)
        session.commit()
        print("\nPurchase added to database!")
        print("------------------------------------")
        print("Would you like to log another purchase? (yes/no)")
        user_input = input("\n> ")
        if user_input in ["yes", "ye", "y"]:
            continue
        elif user_input in ["no", "n"]:
            break


def create_owner_sub():
    while True:
        print("Is Owner registered in system? (yes/no)")
        print("* Enter EXIT to return to Main Menu.")
        owner_exist = input("\n> ")
        if owner_exist in ["yes", "ye", "y"]:
            member_phone = input("Enter owner's phone number: ")
            phone_exists = session.query(Human).filter(Human.phone == member_phone).first()
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
                if user_input in ["yes", "ye", "y"]:
                    continue
                elif user_input in ["no", "n"]:
                    break
        if owner_exist in ["no", "n"]:
            print("Is Dog registered in system? (yes/no)")
            print("* Enter EXIT to return to Main Menu.")
            missing_item = input("\n> ")
            if missing_item in ["yes", "ye", "y"]:
                (dog_name, dog_breed,
                owner_name, owner_phone) = dog_info()
                animal_check = session.query(Dog).filter(Dog.name == dog_name).filter(Dog.breed == dog_breed).first()
                phone_check = session.query(Human).filter(Human.phone == owner_phone).first()
                if animal_check == None:
                    print("Dog does not currently exist in system.")
                    input("Press ENTER add Dog to system...")
                    create_dog_owner(dog_name, dog_breed,
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
                        continue
                    elif user_input in ["no", "n"]:
                        break
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
                        continue
                    elif user_input in ["no", "n"]:
                        break
            elif missing_item in ["no", "n"]:
                input("Press ENTER add Dog to system...")
                create_dog_owner(dog_name, dog_breed,
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


def change_status_on_sub():
    while True:
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
            next_step = input("> ")
            subscription = session.query(Subscription).filter(Subscription.member_id == subscriber.id).first()
            if next_step == "1":
                subscription.status = "Active"
            elif next_step == "2":
                subscription.status = "Deactivated"
            elif next_step == "3":
                while True:
                    try:
                        tier_change = input("Enter tier to change to (1-3): ")
                        if tier_change in ["1", "2", "3"]:
                            subscription.tier = int(tier_change)
                        else:
                            raise ValueError
                    except ValueError:
                        print("\nEntry needs to be either 1, 2, or 3")
                        input("Press ENTER to try entering current tier again...\n")
                    session.commit()
                    break
            elif next_step == "4":
                continue
            elif next_step == "5":
                break
            session.commit()
            print("\nSubscription updated!")
            print("------------------------------------")
            print("Would you like to change another subscription? (yes/no)")
            user_input = input("\n> ")
            if user_input in ["yes", "ye", "y"]:
                continue
            elif user_input in ["no", "n"]:
                break


def app():
    while True:
        menu_choice = menu()
        if menu_choice == "1":
            (dog_name, dog_breed,
            owner_name, owner_phone) = dog_info()
            create_dog_owner(dog_name, dog_breed,
                             owner_name, owner_phone)
        elif menu_choice == "2":
            log_purchase()
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
