# Kanatray

A simple system tray application to manage the `kanata` keyboard remapper.

## Features

*   Start and stop the `kanata` service from the system tray.
*   Select the `kanata` configuration file.
*   Status icon to indicate if `kanata` is running or idle.
*   Cross-platform (Linux, Windows, macOS).

## Installation

1.  **Prerequisites:**
    *   Python 3.6+
    *   `kanata` executable in your system's PATH.
    *   `pip` for installing Python packages.

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application:**

    ```bash
    python main.py
    ```

2.  **Select Configuration File:**
    *   Right-click the tray icon and select "Select Config File".
    *   Choose your `.kbd` file.

3.  **Start/Stop Service:**
    *   Right-click the tray icon and select "Start" to begin the `kanata` service.
    *   The icon will turn green, and the status will update to "Running".
    *   To stop the service, right-click and select "Stop".

## Launching at Startup

To have Kanatray launch automatically when you log in, follow the instructions for your operating system.

### Windows

1.  **Create a Shortcut:**
    *   Right-click on your desktop and select `New > Shortcut`.
    *   In the location field, enter `pythonw.exe <path_to_main.py>`, replacing `<path_to_main.py>` with the full path to the `main.py` file.
    *   Click `Next` and give the shortcut a name (e.g., "Kanatray").

2.  **Add to Startup Folder:**
    *   Press `Win + R` to open the Run dialog.
    *   Type `shell:startup` and press Enter.
    *   Move the shortcut you created into this folder.

### macOS

1.  **Create a Launch Agent:**
    *   Open a text editor and create a new file at `~/Library/LaunchAgents/com.user.kanatray.plist`.
    *   Paste the following content, replacing `<path_to_main.py>` with the full path to the `main.py` file:

        ```xml
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>com.user.kanatray</string>
            <key>ProgramArguments</key>
            <array>
                <string>/usr/bin/python</string>
                <string><path_to_main.py></string>
            </array>
            <key>RunAtLoad</key>
            <true/>
        </dict>
        </plist>
        ```

2.  **Load the Agent:**
    *   Open a terminal and run `launchctl load ~/Library/LaunchAgents/com.user.kanatray.plist`.

### Linux (GNOME, KDE, etc.)

1.  **Create a `.desktop` File:**
    *   Create a file named `kanatray.desktop` in `~/.config/autostart/`.
    *   Paste the following content, replacing `<path_to_main.py>` with the full path to the `main.py` file:

        ```ini
        [Desktop Entry]
        Type=Application
        Exec=python <path_to_main.py>
        Hidden=false
        NoDisplay=false
        X-GNOME-Autostart-enabled=true
        Name[en_US]=Kanatray
        Name=Kanatray
        Comment[en_US]=Start Kanatray at login
        Comment=Start Kanatray at login
        ```

2.  **Make it Executable:**
    *   Open a terminal and run `chmod +x ~/.config/autostart/kanatray.desktop`.