import subprocess
import tkinter as tk
from tkinter import messagebox
from screeninfo import get_monitors

def get_monitor_info():
    # Get information about all monitors
    monitors = get_monitors()
    
    # For simplicity, let's assume you want to use the first monitor
    if monitors:
        return monitors[0]  # Return the first monitor
    else:
        return None  # No monitors found

def get_dialog_position(monitor):
    if monitor:
        # Get the monitor's width and height
        width = monitor.width
        height = monitor.height
        
        # Calculate x and y positions based on monitor resolution
        x = 1090
        if width == a_resolution_width and height == a_resolution_height:            
            y = 910
        # else if width == b_resolution_width and height == b_resolution_height:
        else:            
            y = 1010
        
        window_width = 100
        window_height = 26
        return f"{window_width}x{window_height}+{x}+{y}"
    else:
        return "1090x810"  # Default position if no monitor is found

# Define your monitor resolutions and corresponding x, y offsets
a_resolution_width = 1920
a_resolution_height = 980
x_a = 100
y_a = 0

b_resolution_width = 2560
b_resolution_height = 1080
x_b = 100
y_b = 100

default_x = 100
default_y = 100

def show_custom_dialog(title, message):
    custom_dialog = tk.Toplevel(root)
    custom_dialog.title(title)
    
    # Set background color
    custom_dialog.configure(bg="lightblue")
    
    # Get monitor information
    monitor = get_monitor_info()
      
    # Set the position of the dialog window
    position = get_dialog_position(monitor)
    
    # Set the position of the dialog window
    position = get_dialog_position(monitor)
    custom_dialog.geometry(position)
    
    # Create a Label with a custom background color
    label = tk.Label(custom_dialog, text=message, bg="lightblue", padx=4, pady=4)
    label.pack()
    
    return custom_dialog  # Return the dialog reference    

def close_custom_dialog():
    custom_dialog = store.get_global_value("custom_dialog")
    if custom_dialog:
        custom_dialog.destroy()

def toggle_xbindkeys():    
    if is_xbindkeys_running():
        close_custom_dialog()        
        subprocess.call(["killall", "xbindkeys"])
    else:
        subprocess.Popen(["xbindkeys"])
        custom_dialog = show_custom_dialog("ijkl as arrow activated", "HJKL is arrow")
        store.set_global_value("custom_dialog", custom_dialog)

# Replace is_xbindkeys_running with your implementation
def is_xbindkeys_running():
    # Check if xbindkeys process is running
    try:
        subprocess.check_output(["pidof", "xbindkeys"])
        return True
    except subprocess.CalledProcessError:
        return False
        
        
# Create the main application window
root = tk.Tk()
root.withdraw()  # Hide the main window

toggle_xbindkeys()

# Start the tkinter main loop
root.mainloop()
