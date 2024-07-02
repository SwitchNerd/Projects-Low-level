import psutil
import time
start_time = 0 
exit_time = 0
flag = True
while flag:
    flag = False
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'Discord.exe':
            flag = True
            if start_time == 0:
                start_time == time.time()
            
    if flag == False:            
        exit_time = time.time() 
Seconds_spent = exit_time - start_time                  
# come back to this later
# def not how u do it cause it takes 30% of the cpu lol, works tho