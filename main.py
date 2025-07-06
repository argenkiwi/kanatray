import os
import subprocess
from tkinter import filedialog, Tk
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image, ImageDraw

# --- Configuration ---
APP_NAME = "Kanatray"
CONFIG_FILE_PATH = os.path.expanduser("~/.kanatray_config")

# --- Global State ---
kanata_process = None
config_file = ""
status = "Idle"

def create_image(width, height, color1, color2):
    """Create a simple image for the tray icon."""
    image = Image.new("RGB", (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle((width // 2, 0, width, height // 2), fill=color2)
    dc.rectangle((0, height // 2, width // 2, height), fill=color2)
    return image

def get_icon_image():
    """Returns the icon image based on the status."""
    if status == "Running":
        return create_image(64, 64, "black", "green")
    elif status == "Idle":
        return create_image(64, 64, "black", "grey")
    else:  # Error
        return create_image(64, 64, "black", "red")

def update_menu():
    """Updates the tray menu based on the current state."""
    global tray_icon
    menu_items = [item(f"Status: {status}", None)]
    if status == "Running":
        menu_items.append(item("Stop", on_start_stop))
    elif status == "Idle":
        menu_items.append(item("Start", on_start_stop))
    else:
        menu_items.append(item("Select Config File", on_select_config))

    menu_items.append(item("Quit", on_quit))
    tray_icon.menu = menu(*menu_items)
    tray_icon.icon = get_icon_image()

def start_kanata():
    """Starts the kanata process."""
    global kanata_process, status
    if not config_file:
        status = "Config file not selected"
    else:
        try:
            kanata_process = subprocess.Popen(["kanata", "-c", config_file])
            status = "Running"
        except FileNotFoundError:
            status = "kanata not found"
        except Exception as e:
            status = f"Error: {e}"

def stop_kanata():
    """Stops the kanata process."""
    global kanata_process, status
    if kanata_process:
        kanata_process.terminate()
        kanata_process = None
        status = "Idle"

def on_start_stop(icon, item):
    """Starts or stops the kanata process."""
    if kanata_process:
        stop_kanata()
    else:
        start_kanata()
    update_menu()

def on_select_config(icon, item):
    """Opens a file dialog to select the kanata config file."""
    global config_file, status
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select Kanata Configuration File",
        filetypes=(("Kanata Config", "*.kbd"), ("All files", "*.*")),
    )
    root.destroy()
    if file_path:
        config_file = file_path
        save_config(config_file)
        if kanata_process is None:
            status = "Idle"
    update_menu()

def on_quit(icon, item):
    """Exits the application."""
    if kanata_process:
        kanata_process.terminate()
    icon.stop()

def save_config(path):
    """Saves the config file path."""
    with open(CONFIG_FILE_PATH, "w") as f:
        f.write(path)

def load_config():
    """Loads the config file path."""
    global config_file
    if os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, "r") as f:
            config_file = f.read().strip()

def main():
    """Main application entry point."""
    global tray_icon, status
    load_config()
    if config_file:
        start_kanata()
    else:
        status = "Config file not selected"
    tray_icon = icon(APP_NAME, icon=get_icon_image(), title=APP_NAME)
    update_menu()
    tray_icon.run()

if __name__ == "__main__":
    main()