#dialog.info_dialog("Window title", "content")
import subprocess

def run_command():
    command = ['rofi', '-show', 'window']
    subprocess.run(command, check=True)
    
run_command()