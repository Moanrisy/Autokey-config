import subprocess

script_path = "/home/mars/Dropbox/Scripts/run-with-sudo.sh"

def is_test_script_running():
    # Check if the test-script process is running
    try:
        subprocess.check_output(["pgrep", "-f", f"bash {script_path}"])
        return True
    except subprocess.CalledProcessError:
        return False
        
def toggle_test_script():
    if is_test_script_running():
        subprocess.call(["pkill", "-f", f"bash {script_path}"])
        winTitle = window.get_active_title()
        winClass = window.get_active_class()
        dialog.info_dialog("KILLED", "KILLED:\\nTitle: '%s'\\nClass: '%s'" % (winTitle, winClass))
        print("Bash script killed")
    else:
        # subprocess.Popen(["bash", script_path])
        winTitle = window.get_active_title()
        winClass = window.get_active_class()
        dialog.info_dialog("RUNNING", "RUNNING:\\nTitle: '%s'\\nClass: '%s'" % (winTitle, winClass))
        subprocess.run(['bash', script_path])
        print("Bash script started")

toggle_test_script()