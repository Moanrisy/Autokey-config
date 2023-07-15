import subprocess

def volume_down_kde():
    command = ['qdbus', 'org.kde.kglobalaccel', '/component/kmix', 'invokeShortcut', 'decrease_volume']
    subprocess.run(command, check=True)
    
volume_down_kde()