# Run this script as root 
  
import time 
from datetime import datetime as dt 
  
# change hosts path according to your OS 
hosts_path = "/etc/hosts"
# localhost's IP 
redirect = "127.0.0.1"
  
# websites That you want to block 
website_list = ["www.geeksforgeeks.org", 
      "www.gmail.com","www.outlook.com", 
      "www.moodle.coep.org.in","www.coep.org.in"] 
  
print("""
        1. Block Websites
        2. Unblock Websites
        Enter 1/2 :
        """)
x = int(input())
if x == 1:
    with open(hosts_path, 'r+') as file: 
        content = file.read() 
        for website in website_list: 
            if website in content: 
                pass
            else: 
                # mapping hostnames to your localhost IP address 
                file.write(redirect + " " + website + "\n") 
        print("Blocked Websites")

elif x == 2:
     with open(hosts_path, 'r+') as file: 
            content=file.readlines() 
            file.seek(0)
            for line in content: 
                if not any(website in line for website in website_list): 
                    file.write(line) 
  
            # removing hostnmes from host file 
            file.truncate()
            print("Unblocked sites")

else:
    print("Invalid Option")
    pass
