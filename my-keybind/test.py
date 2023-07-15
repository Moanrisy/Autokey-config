# Enter script code
import subprocess
    
def simulate_media_key(media_key):
    dialog.info_dialog("Window information", "Active window information")
    subprocess.run(['xdotool', 'key', media_key])

def play_pause():
    simulate_media_key('XF86AudioPlay')

def next_track():
    simulate_media_key('XF86AudioNext')

def previous_track():
    simulate_media_key('XF86AudioPrev')

play_pause()