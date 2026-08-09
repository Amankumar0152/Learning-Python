import pyautogui
import time

print("Message will start sending in 5 seconds after program run...")
time.sleep(5)

message = "write your sabitciniya in python"
total_messages = 100

for i in range(total_messages):
    pyautogui.typewrite(message, interval=0.01)  # 0.05 → 0.01
    pyautogui.press('enter')
    # time.sleep(1)  ← enable for a delay between messages