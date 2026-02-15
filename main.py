import json
import os

def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            content = f.read()
            if content.strip() == "":
                return []
            return json.loads(content)
    return []

def save_data(customers):
    with open("data.json", "w") as f:
        json.dump(customers, f)


def add_customer(name, visa_type): # option 1
    if name.strip() == "" :
        print("The name cannot be empty")
        return
    customer = {
        "id": len(customers) + 1,
        "name": name,
        "visa_type": visa_type,
        "status": "Posted"
    }
    customers.append(customer)
    save_data(customers)
    print(f"The Customer '{name}' Added.")

customers = load_data()

def show_customers(): # option 2
    if len(customers) == 0:
        print("No customer submitted")
        return
    for c in customers:
        print(f"{c['id']}. {c['name']} | {c['visa_type']} | {c['status']}.")

def change_status(cid): # option 3
    for c in customers:
        if c["id"] == cid:
            print(f"Status: {c['status']}")
            print("1. Approved")
            print("2. Rejected")
            print("3. Sent to IMM")
            choice = input("New Status: ")
            if choice == "1":
                c["status"] = "Approved"
            elif choice == "2":
                c["status"] = "Rejected"
            elif choice == "3":
                c["status"] = "Sent to IMM"
            else:
                print("Invalid selection.")
                return
            save_data(customers)
            print("The status changed.")
            return
    print("Customer not found.")

def delete_customer(did):
    for d in customers:
        if d["id"] == did:
            customers.remove(d)
            save_data(customers)
            print("Customer removed.")
            return
    print("Customer not found.")


while True:
    print("\n1. Adding Customer")
    print("2. The Customer List")
    print("3. Change Visa Status")
    print("4. Remove Visa")
    print("5. Exit")
    choice = input("Select: ")

    if choice == "1":
        name = input("Customer Name: ")
        print("Visa Type:")
        print("  1. 1M Tourist")
        print("  2. 2M Tourist")
        print("  3. 1M Business")
        visa_choice = input("Select: ")
        visa_types = {
            "1": "1M Tourist",
            "2": "2M Tourist",
            "3": "1M Business"
        }
        if visa_choice not in visa_types:
            print("Invalid Selection.")
        else:
            add_customer(name, visa_types[visa_choice])    
    
    elif choice == "2":
        show_customers()

    elif choice == "3":
        show_customers()
        cid = input("Enter Customer Number: ")
        if cid.strip() == "":
            print("The Number cannot be empty!")
        else:
            change_status(int(cid))

    elif choice == "4":
        did = input("Enter Customer Number: ")
        if did.strip() == "":
            print("The Number cannot be empty.")
        else:
            delete_customer(int(did))
        

    elif choice == "5":
        break