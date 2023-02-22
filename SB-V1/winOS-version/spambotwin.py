from pynput.keyboard import Key, Controller
import time
import subprocess

message = input("Entrez le message à envoyer: ")
print("1. inter = 0.1")
print("2. inter = 0.2")
print("3. inter = 0.3")
print("4. inter = 0.4")
print("5. inter = 0.5")
print("6. inter = 0.6")
print("7. inter = 0.7")
print("8. inter = 0.8")
print("9. inter = 0.9")
print("10. inter = 10")
inter = input("Selectionnez l'interval entre les messages : ")

subprocess.call(["open", "-a", "Firefox"])

keyboard = Controller()

while 1:
    keyboard.type(message)
    if inter == "1":
        time.sleep(0.1)
    elif inter == "2":
        time.sleep(0.2)
    elif inter == "3":
        time.sleep(0.3)
    elif inter == "4":
        time.sleep(0.4)
    elif inter == "5":
        time.sleep(0.5)
    elif inter == "6":
        time.sleep(0.6)
    elif inter == "7":
        time.sleep(0.7)
    elif inter == "8":
        time.sleep(0.8)
    elif inter == "9":
        time.sleep(0.9)
    elif inter == "10":
        time.sleep(1)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

