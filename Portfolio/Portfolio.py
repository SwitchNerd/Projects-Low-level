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
    
    file = open('Portfolio/list.txt', 'a')
    file.write(f'\nProject : {count+1}')
    time.sleep(0.5)
    file.write(f'\nName: {input("Enter a project name: ")}')
    time.sleep(0.5)
    file.write(f'\nDescription: {input("Enter a brief project description: ")}')
    time.sleep(0.5)
    file.write(f'\nCreation Date: {input("Enter the date the project was created (##/##/####): ")}')
    file.close()
def read():
    pass

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
        pass
    elif C1 == 'n':
        clear()
        write()
        clear()
    else:
        print("ERROR : UNEXPECTED ARGUMENT :(")
    
main()