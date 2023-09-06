import subprocess

script_path = "/home/mars/Dropbox/Scripts/custom-resolution.sh"

dialog.info_dialog("RUNNING", "Run custom resolution")
subprocess.run(['bash', script_path])