from models import (session, Dog, Human)
import time


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
            break
        else:
            print("\nDog and breed combo already exists in database.")
            print("Enter info for dog not currently in system.\n")
            (dog_name, dog_breed,
            owner_name, owner_phone) = dog_info()
            continue
