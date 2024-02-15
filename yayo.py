import time
import psutil
import os
from datetime import datetime

    #time.sleep(1)
    #os.system('clear')

def get_cpu():
    print("\n", "*"*20, "CPU INFO","*"*20, "\n")
    print(f"CPU load: {psutil.cpu_percent()}%")
    
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        i+=1
        print(f"cpu{i}:{percentage}%", int(percentage)*"|")
        
def human_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["","K","M","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_mem():
    print("\n","*"*20, "MEMORY INFO","*"*20, "\n")

    mem = psutil.virtual_memory()
    print(f"RAM total: {human_size(mem.total)}")
    print(f"RAM available: {human_size(mem.available)}")
    print(f"RAM usege: {human_size(mem.used)}")

    print(f"{mem.percent}%")

    swap = psutil.swap_memory()
    print(f"swap total: {human_size(swap.total)}")
    print(f"swap used: {human_size(swap.used)}")

def main():
    while True:
        get_cpu()
        get_mem()
        time.sleep(0.8)
        os.system('clear')

if __name__=="__main__":
     main()    
