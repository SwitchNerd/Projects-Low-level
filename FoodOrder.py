import time
import sys

menu = ["Friend salmon patties", "Pancakes with maple syrup", "Steak and eggs", "Country ham & eggs", "Farmer's smoke sausage skillet", "Roast turkey"]
price = [4,3,4,3,5,7]
stock = [6,3,10,5,7,3]
userC = 0
userD = 0
userN = 0
def orderFunc(order, number, ):
    order = order - 1
    if stock[order] >= number:
        totalP = price[order] * number
        print(f'This will come to a total of: ${totalP}')
        if input('Would you like to pay?: ') == 'yes':
            cookingFunc(menu[order])
            return True
        else:
            return False
        
    else:
        print("Out of stock")
        return False
    
def cookingFunc(food):
    print(f"Preparing your {food}")
    for i in range(1,10):
        sys.stdout.write('\rCooking .')
        time.sleep(0.1)
        sys.stdout.write('\rCooking ..')
        time.sleep(0.1)
        sys.stdout.write('\rCooking ...')
        time.sleep(0.1)
    sys.stdout.write('\rDone!      \n')

print("Welcome to the shack")
while userC != 4: 
    userC = input("What would you like to do? \nOrder -1, Talk -2, Check wallet -3, Leave -4: ")
    match int(userC):
        case 1: 
            print("The menu consists of:")
            for i in range (1,6):
                print(f'Item ({i}): {menu[i-1]}, Price: ${price[i-1]}')
                time.sleep(1)  
            userD = int(input("Enter the number ID of the item you would like to order: "))
            userN = int(input("Enter the quantity of the item you would like to order: "))
            orderResult = orderFunc(userD, userN)
            if orderResult == True:
                stock[userD-1] = stock[userD-1] - userN
                time.sleep(1)
                print(f"Here you go, {userN} {menu[userD-1]}!")
                time.sleep(1.5)
        case 2: 
            print("Mhm... This rusty old place is closing soon..")
            time.sleep(1)
            print("Why you ask? The earthquake.. its destroying our customers..")
        case 3: 
            print("You have checked your wallet") #Placeholder code
        case 4: break 
    
        