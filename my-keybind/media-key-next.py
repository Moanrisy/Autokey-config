import subprocess
    
def simulate_media_key(media_key):
    time.sleep(0.5)
    subprocess.run(['xdotool', 'key', media_key])

def next_track():
    simulate_media_key('XF86AudioNext')

next_track()