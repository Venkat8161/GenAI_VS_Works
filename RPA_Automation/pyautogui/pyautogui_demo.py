import pyautogui
import time

#mouse operations
#pyautogui.click(100,100)
#time.sleep(2)
#pyautogui.rightClick(120,120)

time.sleep(2)

#x,y = pyautogui.position()

#print(f'x: {x},y: {y}')

#pyautogui.click(1779,18)

pyautogui.moveTo(1779,18,duration=1)

pyautogui.click()

time.sleep(5)

pyautogui.write("Python rpa_demo_1.py")

pyautogui.press("enter")

x,y = pyautogui.position()
print(f'x: {x},y: {y}')
pyautogui.moveTo(x,y,duration=1)
pyautogui.click()
time.sleep(5)
x,y = pyautogui.position()
print(f'x: {x},y: {y}')
pyautogui.moveTo(x,y,duration=1)
pyautogui.click()
time.sleep(3)
x,y = pyautogui.position()
print(f'x: {x},y: {y}')
pyautogui.moveTo(x,y,duration=1)
pyautogui.click()
time.sleep(2)
pyautogui.write("Hi Sir How are you?")
time.sleep(2)
x,y = pyautogui.position()
print(f'x: {x},y: {y}')
pyautogui.moveTo(x,y,duration=1)
pyautogui.click()




prices = [100, 250, 90]

def discount(lst):
    return [p * 0.9 for p in lst if p > 100]

print(discount(prices))


