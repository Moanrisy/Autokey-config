import subprocess

def volume_up_kde():
    command = ['qdbus', 'org.kde.kglobalaccel', '/component/kmix', 'invokeShortcut', 'increase_volume']
    subprocess.run(command, check=True)
    
volume_up_kde()