# Enter script code
import subprocess

def focus_or_open_vlc():
    process = subprocess.Popen(['pgrep', '-f', 'vlc'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    if process.returncode == 0:
     # Vlc is already running, focus on the active Vlc window
     dolphin_windows = subprocess.check_output(['wmctrl', '-l', '-p']).decode().splitlines()
     for window in dolphin_windows:
         if any(pid in window for pid in output.decode().split()):
             window_id = window.split()[0]
             subprocess.Popen(['wmctrl', '-ia', window_id])
                         
             # Launch vlc-delete extension
             time.sleep(0.5)
             keyboard.send_keys("<alt>+ir")
             
             break
    else:
        # Dolphin is not running, so open a new instance
        subprocess.Popen(['/usr/bin/vlc', '--started-from-file', '/mnt/storage/Music/with-lyric/'])

focus_or_open_vlc()
