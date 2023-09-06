# Enter script code
import subprocess

def run_emacs_command():
    command = ['emacsclient', '-e', '(org-agenda nil "g")']
    subprocess.run(command, check=True)

def open_agenda_emacs():
    process = subprocess.Popen(['pgrep', '-f', 'emacs'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    if process.returncode == 0:
     # Dolphin is already running, focus on the active Dolphin window
     windows = subprocess.check_output(['wmctrl', '-l', '-p']).decode().splitlines()
     for window in windows:
         if any(pid in window for pid in output.decode().split()):
            # Call the function to run the Emacs command
            run_emacs_command()
            # Focus on Emacs window
            window_id = window.split()[0]
            subprocess.Popen(['wmctrl', '-ia', window_id])
            break
    else:
        # Dolphin is not running, so open a new instance
        subprocess.Popen(['/usr/bin/emacs'])

open_agenda_emacs()
