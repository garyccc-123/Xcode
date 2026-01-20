import pyautogui
import time

print("5秒內把滑鼠移到你要的角落（左上角），自動顯示座標")
time.sleep(5)
print("左上角座標：", pyautogui.position())

print("再給你5秒，移到右下角")
time.sleep(5)
print("右下角座標：", pyautogui.position())