import win32api
import win32con
import threading
import time
import pyautogui
import keyboard

def press_key(vk_code):
    win32api.keybd_event(vk_code, 0, 0, 0)
    time.sleep(0.001)
    win32api.keybd_event(vk_code, 0, win32con.KEYEVENTF_KEYUP, 0)

def detect_and_press(pixel_coords, vk_code):
    while not keyboard.is_pressed('q'):
        if pyautogui.pixel(*pixel_coords) == (255, 0, 228):
            press_key(vk_code)
            print(f"Detected key with VK code {vk_code}")

detection_tasks = [
    ((730, 878), 0x44),  # D key
    ((879, 878), 0x46),  # F key
    ((1032, 878), 0x4A),  # J key
    ((1183, 878), 0x4B),  # K key
]

threads = []
for coords, vk_code in detection_tasks:
    thread = threading.Thread(target=detect_and_press, args=(coords, vk_code))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
