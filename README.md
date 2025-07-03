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
