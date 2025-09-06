# LeftHandedMouse

A Python tool that swaps left and right mouse buttons for left-handed users.  
Runs in the background and cleanly exits on command for an easy accessibility solution.

---

## Features
- Swap left and right mouse buttons
- Run in background silently
- Works on Windows, Linux, and macOS
- Easy to start/stop and customize

---

## Requirements

- Python 3.7+
- [`pynput`](https://pypi.org/project/pynput/)

Install `pynput`:

```bash
pip install pynput ```

## Usage

1. Save the script as lefthanded_mouse.py.
2. Run the script:
```bash
python lefthanded_mouse.py ```

3. The script will swap your mouse buttons. Press Ctrl+C in the terminal to stop

---


## Make it Run on Startup

### Windows

1. Save lefthanded_mouse.py somewhere, e.g., C:\Users\<YourName>\Documents\lefthanded_mouse.py.

2. Create a batch file swap_mouse.bat with:

```bash
@echo off
pythonw "C:\Users\<YourName>\Documents\lefthanded_mouse.py" ```


3. Press Win + R, type shell:startup, and hit Enter.


4. Copy the swap_mouse.bat into the Startup folder.


5. The script will now run automatically at login.



---

### Linux (systemd)

1. Make the script executable:

```bash
chmod +x lefthanded_mouse.py ```


2. Create a systemd service at ~/.config/systemd/user/lefthanded_mouse.service:

```bash
[Unit]
Description=Swap mouse buttons for left-handed use

[Service]
ExecStart=/usr/bin/python3 /home/<yourname>/lefthanded_mouse.py
Restart=always

[Install]
WantedBy=default.target ```


3. Enable and start the service:

```bash
systemctl --user enable lefthanded_mouse.service
systemctl --user start lefthanded_mouse.service ```




---

### macOS

1. Save lefthanded_mouse.py somewhere.


2. Open Automator → Application → add Run Shell Script:

```bash
/usr/bin/python3 /Users/<yourname>/Documents/lefthanded_mouse.py ```


3. Save as SwapMouse.app.

4. Go to System Preferences → Users & Groups → Login Items → add SwapMouse.app.

5. The script will now run at startup.


---

## Notes

The script only works while running. Exiting stops the remapping.

Middle and other buttons remain unchanged.

You can extend the script to add toggle hotkeys for left/right-handed mode.


---

## License

MIT License
