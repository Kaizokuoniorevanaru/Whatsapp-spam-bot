import subprocess
import sys
def install(pakage):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',pakage])

install("pyautogui")
install("tk")
print('''Enter you path of whatsapp for example
if you whatsapp is at you desktop so you write like this
C:\\Users\\vihaa\\Desktop\\WhatsApp.lnk  ''')

a = input("Enter your path:")
b = input("enter num:")
with open("data/path.txt","w") as file:
    file.write(a)
    file.write("\n")
    file.write(b)
    

