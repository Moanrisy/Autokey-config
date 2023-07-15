# Enter script code
import subprocess

def focus_or_open_chrome():
    process = subprocess.Popen(['pgrep', '-f', 'chrome'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    if process.returncode == 0:
     # Chrome is already running, focus on the active Chrome window
     chrome_windows = subprocess.check_output(['wmctrl', '-l', '-p']).decode().splitlines()
     for window in chrome_windows:
         if any(pid in window for pid in output.decode().split()):
             window_id = window.split()[0]
             subprocess.Popen(['wmctrl', '-ia', window_id])
                         
             # Launch vlc-delete extension
             time.sleep(0.5)
             keyboard.send_keys("<shift>+<alt>+d")
             
             break
    else:
        # Dolphin is not running, so open a new instance
        subprocess.Popen(['/usr/bin/google-chrome-stable'])

focus_or_open_chrome()
