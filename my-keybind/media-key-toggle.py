import subprocess
    
def simulate_media_key(media_key):
    time.sleep(0.5)
    subprocess.run(['xdotool', 'key', media_key])

def play_pause():
    simulate_media_key('XF86AudioPlay')

def custom_vlc_media_key_pause():
    process = subprocess.Popen(['pgrep', '-f', 'vlc'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    if process.returncode == 0:
     # Vlc is already running, focus on the active Vlc window
     dolphin_windows = subprocess.check_output(['wmctrl', '-l', '-p']).decode().splitlines()
     for window in dolphin_windows:
         if any(pid in window for pid in output.decode().split()):
                         
             # Play pause VLC config
             time.sleep(0.5)             
             keyboard.press_key("<ctrl>")
             keyboard.press_key("<f11>")
             keyboard.release_key("<f11>")
             keyboard.release_key("<ctrl>")
             
             break
    else:
        play_pause()

custom_vlc_media_key_pause()