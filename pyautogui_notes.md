


<br>

# Examples 

```python
>>> import pyautogui
```

## screen
```python
>>> screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
>>> screenWidth, screenHeight
(2560, 1440)
```

```
0,0       X increases -->
+---------------------------+
|                           | Y increases
|                           |     |
|   1920 x 1080 screen      |     |
|                           |     V
|                           |
|                           |
+---------------------------+ 1919, 1079
```

## mouse 
```python

>>> currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
>>> currentMouseX, currentMouseY
(1314, 345)

>>> pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

>>> pyautogui.click()          # Click the mouse.
>>> pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
>>> pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

>>> pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
>>> pyautogui.doubleClick()     # Double click the mouse.
>>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

>>> pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
>>> pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

>>> with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
        pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
>>> # Shift key is released automatically.

>>> pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

>>> pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.
```

<br>

# Documentation
https://pyautogui.readthedocs.io/en/latest/index.html

<br>

# Install 
https://pyautogui.readthedocs.io/en/latest/install.html

## On Linux, additionally applications are needed
```bash
apt-get install -y \
    scrot `# command line screen capture utility` \
    python3-tk `# Tkinter - Writing Tk applications with Python 3.x` \
    python3-venv `# venv module for python3 (default python3 version)` \
    python3-dev `# header files and a static library for Python (default)` 
```
## pip install 
```bash
python3 -m venv venv; source venv/bin/activate
python3 -m pip install pyautogui
```

<br>

# youtube 

## Python Automation with PyAutoGUI -> Code of the Future
https://www.youtube.com/watch?v=3PekU8OGBCA


## How to make advanced image recognition bots using python
https://www.youtube.com/watch?v=YRAIUA-Oc1Y

win32API for mouse clicks 

### RGB values and position at mouse pointer 
```python
python3
import pyautogui
pyautogui.displayMousePosition 
```

### stop
```python
import keyboard
while keyboard.is_pressed('q') == False:
    blar blar
```








