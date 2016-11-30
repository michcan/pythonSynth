from pynput.keyboard import Key, Listener
from pyo import *

s = Server(audio="pa").boot()
s.start()
a = Sine(mul=0.01).out()

def on_press(key):
    print(ord(key.char))
    a.freq = ord(key.char)*3

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()