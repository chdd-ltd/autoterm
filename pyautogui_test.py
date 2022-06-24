import pyautogui 
import time

# wait before starting
time.sleep(5)

# Screen resolution 
print(pyautogui.size()) # screen size in pixels 
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

# Mouse Fuctions 
print(pyautogui.position()) # print the position of mouse
pyautogui.moveTo(100, 200, 5) # moves mouse to X of 100, Y of 200 over 2 seconds
print(pyautogui.position()) # print the position of mouse

pyautogui.move(0, 50)       # move the mouse down 50 pixels.
print(pyautogui.position()) # print the position of mouse

pyautogui.move(-30, 0)      # move the mouse left 30 pixels.
print(pyautogui.position()) # print the position of mouse

pyautogui.moveRel(100, 100, 3)      # move the mouse relative to its current position 
print("moveRel", pyautogui.position()) # print the position of mouse

