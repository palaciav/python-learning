import time
from datetime import datetime as dt

hosts_path = "C:\Windows\system32\drivers\etc"
redirect="127.0.0.1"
websites_list = ["www.facebook.com","www.hotmail.com","facebook.com","hotmail.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):

    # Check time here
        print("Working hours...")
    time.sleep(5)