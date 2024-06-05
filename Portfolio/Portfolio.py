import time
from replit import clear
#Getting the project count
with open('Portfolio/list.txt') as temp:   
    data = temp.readline()
    count = int(data[15:16])
#Intialising the variable to check if the file has changed
modified = False

def write():
    #Changing modified to true, as the write command has been called
    global modified 
    modified = True
    #Incrementing count each time another project is added
    global count
    count = count + 1
    print('Creating a new project...')
    time.sleep(1)
    file = open('Portfolio/list.txt', 'a')
    file.write(f'\nProject : {count}')
    time.sleep(0.5)
    file.write(f'\nName: {input("Enter a project name: ")}')
    time.sleep(0.5)
    file.write(f'\nDescription: {input("Enter a brief project description: ")}')
    time.sleep(0.5)
    file.write(f'\nCreation Date: {input("Enter the date the project was created (##/##/####): ")}')
    file.close()
    

def read():
    file = open('Portfolio/list.txt','r')
    
    C2 = int(input("Would you like to view all exisiting projects or a specific one? (1, 2): "))
    if C2 == 1:
        lines = file.readlines()
        # dont do anything to this, takes too long to fix 
        for line in lines:
            if 'Project' in line:
                print('-----------------------')
                print(line.strip())
            else:
                print(line.strip())
    elif C2 == 2:
        pass
    else:
        print("ERROR: UNEXPECTED ARGUMENT")
        time.sleep(1)
        

def main():
    time.sleep(0.5)
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣎⠭⠭⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⣩⠔⣋⣥⠶⠀⠀⠀⣄⠉⠓⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴⠊⠁⠀⢸⠟⣡⠾⠋⠀⣠⡶⠀⠀⢻⣇⣀⣿⡤⠤⠤⣤⣄⣤⣤⠔⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤
⠀⠀⠀⠀⠀⠀⣠⢞⡭⠀⢠⣶⡀⢠⠏⡼⠋⢀⣤⡿⠋⢀⣾⢀⣾⣋⣿⠿⠒⠚⠛⠋⠉⠉⠁⠀⣀⣀⣠⣤⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣾⣴⣏⠀⠀⠈⠻⣷⡼⠀⠀⠰⠟⠁⠀⣰⠿⣣⣾⣧⣴⡿⠶⠆⢀⣠⣤⢶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿
⠀⠀⠀⠀⡴⠛⠉⢹⣧⠀⠀⠀⢈⣿⣄⠀⠀⢠⠴⢛⡡⠞⢉⡩⠟⠀⣠⣴⡾⠋⠉⠀⠈⣿⣿⣽⣿⣿⣿⣿⣛⣛⠿⢿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠀⡷⠒⠉⠉⠉⠁⠲⡖⠉⣿⣿⣷⣤⣴⣮⣭⠴⠒⢉⣤⡶⠛⠉⠀⣿⣴⣦⣄⠀⠻⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀
⠀⠀⢀⡞⣡⡶⠀⠀⠒⢦⡀⠱⣤⣿⣿⠟⠿⠿⠏⠀⣠⣴⣿⣥⣤⣤⣤⣴⠟⣷⠈⠙⠳⣄⠀⠐⢽⡻⢷⣮⣽⣿⣿⣿⣿⣟⠁⣀⣀⠀
⠀⠀⣾⣾⢋⣴⡶⠂⠀⢸⡗⢳⡿⣯⠀⠀⠀⢀⣴⣞⣻⣿⡿⢚⡿⠿⣿⣯⣀⠙⢶⣖⣒⠚⠀⢠⣄⠈⢦⠈⠙⠻⣿⡟⠁⠈⠉⢀⣼⠤
⠀⠀⢿⠃⣼⠟⢀⣼⡇⣾⢃⣾⠁⠿⢃⠖⣠⡿⢿⣾⠟⢹⣧⣬⣽⡿⣫⠿⠯⢷⡈⠛⠛⡃⠀⣷⡈⣦⡈⡇⠀⠀⠈⢳⣄⡀⠀⠀⠀⠀
⠀⠀⠈⢾⣏⢀⣼⣋⡴⢛⡿⠁⢀⠞⣡⣾⣿⡀⠀⠑⠒⠀⠀⠀⠉⠋⠀⠀⠀⠀⠹⡀⠀⠹⡔⠻⣿⡏⠁⣹⣄⠀⠀⠀⠙⢿⠒⠤⣀⠀
⠀⠀⠀⠀⠈⠙⠛⠣⣶⡟⠁⡰⢃⡴⠿⣛⣿⣷⣤⠶⠦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣇⢠⡤⢧⢠⠟⢀⡰⠃⠘⠢⡀⠀⢱⡈⠆⢢⠀⠙
⠀⠀⠀⠀⠀⠀⠀⣰⣿⢀⠞⣡⣿⣀⣴⢿⣽⣿⡇⠀⠀⢀⣸⡀⠀⠀⠀⠀⠀⠀⠀⠘⠀⢇⠘⣿⣶⡏⠀⠀⢤⡀⠈⢢⠀⢷⡘⠈⡄⠀
⠀⠀⠀⠀⠀⠀⣴⠉⣩⢃⣼⡇⠈⢩⠁⠈⠻⡼⣧⣄⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢻⠉⡇⠀⠀⢠⢹⡦⡀⢣⠘⣇⠸⠇⠀
⠀⠀⠀⠀⠀⣰⢃⡜⢡⡞⠋⠻⣾⣏⠀⠀⠀⢿⣄⣨⡽⠿⢻⠿⠿⢷⣦⠀⠀⠀⠀⠀⠀⣠⣄⡸⠀⣿⣦⣄⠀⠳⣵⡌⠢⡇⢸⠁⠀⠀
⠀⠀⠀⠀⣰⣣⠋⣰⣿⡇⠀⢀⠨⢿⣄⠀⠀⠀⠉⢟⢶⣖⠋⣀⡤⠖⠋⠀⡀⠀⠀⠀⠰⡇⢸⠇⠀⣿⣿⣿⣦⡀⠙⣿⡄⢹⠸⡇⠀⠀
⠀⠀⠀⣼⡿⢁⣾⠯⣿⣧⣠⡸⣄⠀⠻⡆⠀⠀⠀⠈⠃⠛⠛⠉⠀⠀⣀⣼⠇⠀⠀⠀⠀⢹⠏⠀⢠⣿⣿⣿⣿⣿⣄⠈⢧⢸⣾⡇⠀⠀
⠀⢀⡼⠋⣠⣿⣿⡄⣿⣿⣿⡄⠈⢻⡗⣻⣶⣄⠀⠀⠀⢰⣤⣴⠾⠛⠉⠁⠀⢠⡒⠉⢷⡿⠀⠀⣼⣯⣟⢿⣿⣿⣿⣷⣼⣿⣿⠀⠀⢀
⢀⠞⢁⣼⣿⣿⣿⣣⣿⣿⣿⣇⠀⠀⡟⢻⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⣴⢻⠃⠀⢀⣿⣿⣿⣧⠉⢻⣿⣿⣿⠃⠁⠀⢀⣌
⠏⣠⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⣇⢸⢿⣿⣿⣿⣷⣤⡒⢆⠀⠀⢀⣠⣴⣾⡿⢁⡎⠀⠀⣼⠿⣿⣿⣿⣇⢸⣿⣿⡇⠀⠀⢠⡿⠃
⣾⣿⠿⠟⣛⣿⣿⣿⣿⣿⣿⣿⣇⠀⢻⣾⢸⡘⣿⣿⣿⣿⣿⣬⣷⣾⣿⣿⣿⠟⠀⠈⠀⠀⢠⡿⠀⢻⣿⣟⣿⢸⣿⣿⠃⠀⣰⡿⠁⠀
⠀⣠⠴⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⡄⠈⣿⡀⢷⣿⣿⡟⣿⣿⣿⣧⣿⣿⡿⠋⠀⠀⠀⠀⢠⣿⡇⢠⣿⢟⣾⠟⣸⣿⡿⢀⣼⡿⠃⠀⠀
⠉⠀⠀⠉⣉⠽⠋⠉⢀⡤⢈⠏⢻⣧⠀⢹⣇⠘⣿⣿⣷⣏⡿⣿⣸⣿⡿⠁⠀⠀⠀⠀⢠⡿⢻⣥⣿⣿⣿⡟⢰⣿⡟⢡⡾⡽⠁⠀⠀⠐
⠙⢿⣿⣞⠙⢷⣶⣿⡿⠖⠉⢀⡄⠹⡄⠈⢟⡆⢸⣟⢿⣿⣿⣿⣿⣽⣇⠀⠀⠀⠀⠀⠘⠃⣾⣷⣿⣿⡟⢠⡿⠋⡰⢋⡞⢁⡠⠂⢈⡆''')
    time.sleep(1)
    print("\nPS: For any boolean questions, answer with 'y' or 'n'")
    time.sleep(1.5)
    C1 = input("Would you like to view exisiting projects?: ")
    if C1 == 'y':
        clear()
        read()
    elif C1 == 'n':
        clear()
        write()
    else:
        print("ERROR : UNEXPECTED ARGUMENT")
        time.sleep(1)
        
    
        

main() 
if modified:
    with open("Portfolio/list.txt", "r+") as f:
     old = f.read() # read everything in the file
     postString = old.split("\n",1)[1]
     f.seek(0) # rewind
     f.write(f"ProjectCount = {count}\n" + postString) # write the new line before
# Create a new file with same name, everything the same exxcept the first line with the new count