import time
import pynput.mouse
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()
print(mouse.position)
first = (909, 851)
mid = (1233, 716)
new = (1105, 855)
second = (1237, 372)
third = (1494, 397)
four = (1483, 475)

def fun():
    mouse.position = new
    mouse.click(Button.left, 1)
    time.sleep(.1)
    keyboard.press(Key.down)
    time.sleep(.1)

def fun2(i):
    mouse.position = second
    mouse.click(Button.left, 1)
    time.sleep(.1)
    for _ in range(i + 1):
        keyboard.press(Key.down)
        time.sleep(.2)

def loop(y):
    mouse.position = first
    for _ in range(y):
        mouse.click(Button.left, 1)
        time.sleep(.3)
def book(book_pages):
    for i in range(book_pages):
        mouse.position = third
        mouse.click(Button.right, 1)
        time.sleep(.4)
        mouse.position = four
        mouse.click(Button.left, 1)
        time.sleep(.4)

        if i <= 23:
            fun2(i)
        else:
            fun()

# loop(500)
book(27)

