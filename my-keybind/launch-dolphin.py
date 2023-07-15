# Enter script code
import subprocess

def focus_or_open_dolphin():
    process = subprocess.Popen(['pgrep', '-f', 'dolphin'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    if process.returncode == 0:
     # Dolphin is already running, focus on the active Dolphin window
     dolphin_windows = subprocess.check_output(['wmctrl', '-l', '-p']).decode().splitlines()
     for window in dolphin_windows:
         if any(pid in window for pid in output.decode().split()):
             window_id = window.split()[0]
             subprocess.Popen(['wmctrl', '-ia', window_id])
             break
    else:
        # Dolphin is not running, so open a new instance
        subprocess.Popen(['/usr/bin/dolphin'])

focus_or_open_dolphin()
