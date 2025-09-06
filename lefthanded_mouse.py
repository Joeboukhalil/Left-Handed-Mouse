from pynput import mouse
import threading
import signal
import sys

# Create a controller to send mouse events
controller = mouse.Controller()

# Flag to control remapping
remap_enabled = True

def on_click(x, y, button, pressed):
    if not remap_enabled:
        return True  # Let normal events through

    # Swap left and right clicks
    if button == mouse.Button.left:
        swapped_button = mouse.Button.right
    elif button == mouse.Button.right:
        swapped_button = mouse.Button.left
    else:
        return True  # Don’t block middle button

    if pressed:
        controller.press(swapped_button)
    else:
        controller.release(swapped_button)

    return False  # Suppress original click

def start_listener():
    with mouse.Listener(on_click=on_click, suppress=True) as listener:
        listener.join()

def signal_handler(sig, frame):
    print("\nMouse remapping stopped. Exiting gracefully.")
    sys.exit(0)

if __name__ == "__main__":
    print("Left/Right mouse remapping active. Press Ctrl+C to stop.")
    signal.signal(signal.SIGINT, signal_handler)
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.start()
