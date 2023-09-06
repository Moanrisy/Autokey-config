import subprocess

def is_xbindkeys_running():
    # Check if xbindkeys process is running
    try:
        subprocess.check_output(["pidof", "xbindkeys"])
        return True
    except subprocess.CalledProcessError:
        return False

def toggle_xbindkeys():
    if is_xbindkeys_running():
        subprocess.call(["killall", "xbindkeys"])
        #dialog.info_dialog("Window information", "xbindkeys killed")
    else:
        subprocess.Popen(["xbindkeys"])
        dialog.info_dialog("ijkl as arrow activated", "xbindkeys started")
        
toggle_xbindkeys()
        
