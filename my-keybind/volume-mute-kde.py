import subprocess

def volume_mute_kde():
    command = ['qdbus', 'org.kde.kglobalaccel', '/component/kmix', 'invokeShortcut', 'mute']
    subprocess.run(command, check=True)
    
volume_mute_kde()