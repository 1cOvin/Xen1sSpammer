import pyautogui
import time

time.sleep(3)





print('''
▒██   ██▒▓█████  ███▄    █   ██████ 
▒▒ █ █ ▒░▓█   ▀  ██ ▀█   █ ▒██    ▒ 
░░  █   ░▒███   ▓██  ▀█ ██▒░ ▓██▄   
 ░ █ █ ▒ ▒▓█  ▄ ▓██▒  ▐▌██▒  ▒   ██▒
▒██▒ ▒██▒░▒████▒▒██░   ▓██░▒██████▒▒
▒▒ ░ ░▓ ░░░ ▒░ ░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░
░░   ░▒ ░ ░ ░  ░░ ░░   ░ ▒░░ ░▒  ░ ░
 ░    ░     ░      ░   ░ ░ ░  ░  ░  
 ░    ░     ░  ░         ░       ░''')
print("[+] Welcome To Xen1s Discord Text Spammer [+]")
print("==============================================")

message = input("[+] What Message Do You Wanna Spam? [+]")
repeats = int(input("[+] How Many Times Do You Wanna Spam The Messages? [+]"))
delay = int()

time.sleep(5)

for i in range(0,repeats):
    if message != "":
        pyautogui.typewrite(message)
        pyautogui.press("enter")
    else:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")

    time.sleep(delay/100)

print('''



[+] Completed!, Re-open The Program If You Wanna Spam Again. Closing in 10 Seconds [+]


''')

time.sleep(10)
