#Save contacts, open contacts, Save contact, delete contact
#Contact has a name, phone number, any extra detail


# cd onedrive\desktop\projects\Contact
import time

userC = 0


def deleteBook():
    #Code this later thanks : ) ) ) ) ) ) )
    pass

def writeBook(name, phn, notes):
    with open('contact.txt', 'a') as file:
        file.write(f'{name}|{phn}|{notes}\n')
        
def openBook():
    userC3 = int(input("Would you like to list all contacts or search for one? (1,2): "))
    if userC3 == 1:
        with open('contact.txt', 'r') as file:
            for line in file.readlines():
                name, phn, notes = line.split("|")
                print(f'Name: {name}, Number: +94{phn}, Notes: {notes}')
                time.sleep(0.5)
            time.sleep(0.5)
        file.close()
    elif userC3 == 2:  
        userC2 = input("Would you like to search the contact by name or phone: ")
        userC2 = userC2.upper()
        openContact(userC2)
        
def openContact(userC2):
    match userC2:
        case 'NAME':
            c4 = searchContact(input("Enter the name correctly: "), 2)
            if not c4:
                print("Eror: Couldnt find, retry")
        case 'PHONE':
            c4 = searchContact(input('Enter phone correctly: +94 '), 1)
            if not c4:
                print("Eror: Couldnt find, retry")

def searchContact(placeholder ,dec):
    with open('contact.txt', 'r') as file:
            for line in file.readlines():
                name, phn, notes = line.split("|")
                if dec == 2:
                    if name == placeholder:
                        print(f'Name: {name}, Number: +94{phn}, Notes: {notes}')
                        return True
                elif dec == 1:
                    if phn == placeholder:
                        print(f'Name: {name}, Number: +94{phn}, Notes: {notes}')
                        return True

def main():
    while True :
        userC = int(input("Enter a choice: \n1: Create new contact 2: List/Open existing contacts 3: Delete exisiting contact, 4: Exit "))
        match userC:
            case 1:
                writeBook(input("Enter a name: "), int(input("Enter a phone number: +94 ")), input("Enter any notes: "))
            case 2:
                openBook()
            case 3:
                pass
            case 4:
                break
main()