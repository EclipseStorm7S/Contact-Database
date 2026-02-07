import firebase_admin
from firebase_admin import firestore

cred = firebase_admin.credentials.Certificate("apikey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

running = True
while running:
    print("Welcome! Would you like to view, create, or delete contact info?n\n1) View\n2) Create\n3) Edit\n4) Delete\n5) Exit")
    choice = input(">>")

    match choice:
        case "1":
            print("Viewing contact info...")
            contact_query = db.collection("Contacts").stream()
            for contact in contact_query:
                condict = contact.to_dict()
                print("\n--------------------\n")
                print(f"{condict['FName']} {condict['LName']}")
                if ("PhoneNum" in condict): print(f"Phone: {condict['PhoneNum']}")
                if ("AltNum" in condict): print(f"Alternate Phone: {condict['AltNum']}")
                if ("Email" in condict): print(f"Email: {condict['Email']}")
                if ("Address" in condict): print(f"Address: {condict['Address']}")
            print("\n--------------------\n")
        case "2":
            print("Enter contact info. Leave field blank to omit (First name and Last name cannot be omitted.)")
            fname = input("First Name: ")
            contactinfo = {"FName" : fname}
            lname = input("Last Name: ")
            if lname != "": contactinfo["LName"] = lname
            PhNum = input("Phone Number: ")
            if PhNum != "": contactinfo["PhoneNum"] = PhNum
            AltNum = input("Alternate Phone Number: ")
            if AltNum != "": contactinfo["AltNum"] = AltNum
            Email = input("Email: ")
            if Email != "": contactinfo["Email"] = Email
            Address = input("Address: ")
            if Address != "": contactinfo["Address"] = Address

            contacts_ref = db.collection("Contacts")
            contacts_ref.document((fname + lname).lower()).set(contactinfo)
        case "3":
            FileName = input("Enter the first and last name of the contact you want to edit: ")
            contact = db.collection("Contacts").document(FileName.replace(" ","").lower())
            condict = contact.get().to_dict()
            print("\n--------------------\n")
            print(f"{condict['FName']} {condict['LName']}")
            if ("PhoneNum" in condict): print(f"1) Phone: {condict['PhoneNum']}")
            else: print("4) Phone:")
            if ("AltNum" in condict): print(f"2) Alternate Phone: {condict['AltNum']}")
            else: print("4) Alternate Phone:")
            if ("Email" in condict): print(f"3) Email: {condict['Email']}")
            else: print("4) Email:")
            if ("Address" in condict): print(f"4) Address: {condict['Address']}")
            else: print("4) Address:")
            print("\n--------------------\n")
            choice2 = input("What would you like to update? (1-4):")
            editField = ""
            match choice2:
                case "1": editField = 'PhoneNum'
                case "2": editField = 'AltNum'
                case "3": editField = 'Email'
                case "4": editField = 'Address'
                case _: break
            x = input("Enter new value: ")
            contact.update({editField: x})
            print("Data updated!")
        case "4":
            FileName = input("Enter the first and last name of the contact you want to delete: ")
            if input(f"Are you sure you want to permanently delete {FileName}? (y/n)").lower() == "y":
                db.collection("Contacts").document(FileName.replace(" ","").lower()).delete()
                print("Contact deleted!")
            else:
                print("Contact not deleted.")
        case "5":
            print("Good Bye!")
            running = False
        case _:
            print("Invalid choice. Enter a number between 1 and 5.")
