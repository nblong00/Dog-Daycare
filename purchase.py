from models import (session, Human, Purchase)


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
