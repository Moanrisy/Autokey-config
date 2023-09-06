from pynput.keyboard import Key, Controller
from pynput.mouse import Listener
import subprocess
import time

# Global variable to track whether spam_command is running
spam_command_running = False

def is_spam_command_running():
    global spam_command_running
    return spam_command_running

def toggle_spam_command():
    global spam_command_running
    if is_spam_command_running():
        spam_command_running = False
    else:
        spam_command_running = True

def spam_command():
    keyboard = Controller()
    while True:
        if is_spam_command_running():
            if keyboard.pressed('h'):
                keyboard.press(Key.left)
                keyboard.release(Key.left)
                time.sleep(0.012)
                                # Wait until 'h' key is released
                while keyboard.pressed('h'):
                    pass


toggle_spam_command()
if is_spam_command_running():
    winTitle = window.get_active_title()
    winClass = window.get_active_class()
    dialog.info_dialog("Window information", "RUNNING :\\nTitle: '%s'\\nClass: '%s'" % (winTitle, winClass))
    spam_command()
else:
    winTitle = window.get_active_title()
    winClass = window.get_active_class()
    dialog.info_dialog("Window information", "KILLED :\\nTitle: '%s'\\nClass: '%s'" % (winTitle, winClass))
