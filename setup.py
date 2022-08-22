import subprocess
import sys
def install(pakage):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',pakage])

install("pyautogui")
install("tk")
print('''_________________________________________________________
Enter your path of Whatsapp for example
If your WhatsApp is at your desktop ao you write like this
C:\\User\\Desktop\\Whatsapp.ink
________________________________________________________________ ''')

a = input("Enter your path: ")
print("Dont put secound or sec after number like put 10 for 10sec and so...on")
b = input("Enter that how much time your Whatsapp take to boot in sec: ")
with open("data/path.txt","w") as file:
    file.write(a)
    file.write("\n")
    file.write(b)
    

