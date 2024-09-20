import pyautogui
import keyboard
import time
import threading
import win32gui
import random
import cv2
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)


def move_character(direction, hold_time):
    if direction == "left":
        pyautogui.keyDown("a")
        time.sleep(hold_time)
        pyautogui.keyUp("a")
    elif direction == "right":
        pyautogui.keyDown("d")
        time.sleep(hold_time)
        pyautogui.keyUp("d")


def detect_encounter():
    # Load encounter image
    encounter_img = cv2.imread('assets/encounter.png')

    # Take screenshot of PROClient window (1600x900)
    screenshot = pyautogui.screenshot(region=(0, 0, 1600, 900))
    frame = np.array(screenshot)

    # Use template matching
    result = cv2.matchTemplate(frame, encounter_img, cv2.TM_CCOEFF_NORMED)

    # Check for match
    threshold = 0.55  # Increased threshold
    loc = np.where(result >= threshold)

    # Filter repeated matches
    matches = []
    for pt in zip(*loc[::-1]):
        if len(matches) == 0 or pt[0] > matches[-1][0] + encounter_img.shape[1]:
            matches.append(pt)

    # Print debugging info
    print(f"Encounter detection result: {len(matches) > 0}")
    print(f"Number of matches found: {len(matches)}")

    # Return True if encounter detected
    return len(matches) > 0


class MovementThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.do_run = threading.Event()

    def run(self):
        self.do_run.set()
        focus_window("PROClient")
        direction = "left"
        while self.do_run.is_set():
            hold_time = random.uniform(0.3, 1)  # Adjust key hold time
            move_character(direction, hold_time)
            time.sleep(random.uniform(0.05, 0.15))  # Wait between key presses

            # Check for encounter
            if detect_encounter():
                # Stop movement
                self.do_run.clear()

                # Transition to Encounter Module
                import encounter
                encounter.EncounterModule().start()

            direction = "right" if direction == "left" else "left"


def focus_window(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    win32gui.SetForegroundWindow(hwnd)


movement_thread = None

def hotkey_handler():
    global movement_thread
    while True:
        if keyboard.is_pressed("f11"):
            if movement_thread is None or not movement_thread.is_alive():
                logging.info("Creating new MovementThread instance")
                movement_thread = MovementThread()
                movement_thread.daemon = True
                movement_thread.start()
                time.sleep(0.2)
            else:
                logging.info("MovementThread instance already running")
        elif keyboard.is_pressed("f10"):
            if movement_thread is not None and movement_thread.is_alive():
                movement_thread.do_run.clear()
                time.sleep(0.1)
        time.sleep(0.1)


if __name__ == "__main__":
    hotkey_thread = threading.Thread(target=hotkey_handler)
    hotkey_thread.start()