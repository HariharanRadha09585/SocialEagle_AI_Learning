import pyautogui
import time
import pyscreeze

from playwright.sync_api import sync_playwright
pyautogui.FAILSAFE = True

'''
#Mouse Operationst
#pyautogui.moveTo(100, 100, duration=1)  # Move the mouse to (100, 100) over 1 second
pyautogui.scroll(500)  # Scroll up 500 units
time.sleep(1)  # Wait for 1 second
pyautogui.scroll(500)  # Scroll down 500 units
'''




# Keyboard Operations
'''
pyautogui.typewrite("Hello, this is an automated message!", interval=0.5)  # Type the message with a delay of 0.1 seconds between each character
pyautogui.press("enter")  # Press the Enter key
time.sleep(0.5)  # Wait for 1 second
pyautogui.typewrite("Clear", interval=0.5)  # Type the message with a delay of 0.1 seconds between each character
pyautogui.press("enter")  # Press the Enter key
'''

#hotkey Operations
'''
pyautogui.hotkey('win', 'r')  # Press Win+R to open Run dialog
pyautogui.typewrite("tree", interval=0.5)
pyautogui.press("enter")  # Press the Enter key

pyautogui.hotkey('win', 'r')  # Press Win+R to open Run dialog
pyautogui.typewrite("%temp%", interval=0.5)
pyautogui.press("enter")  # Press the Enter key
pyautogui.hotkey('ctrl', 'a')  # Press Ctrl+A
pyautogui.press("delete")  # Press the Delete key
'''
# Open Applications
'''
pyautogui.press("win")  # Press the Windows key
time.sleep(1)  # Wait for 1 second
pyautogui.typewrite("Revit 2025", interval=0.1)  # Type "Revit 2025" with a delay of 0.1 seconds between each character
time.sleep(1)  # Wait for 1 second
pyautogui.press("enter")  # Press the Enter key
'''

#Capture Screenshot
"""
screenshot = pyautogui.screenshot()  # Capture a screenshot of the entire screen
screenshot.save("test.png")  # Save the screenshot as "screenshot.png"
"""


# Open chrome and search for a keyword
"""
pyautogui.press("win")  # Press the Windows key
time.sleep(1)  # Wait for 1 second
pyautogui.typewrite("Chrome", interval=0.1)  # Type "Chrome" with a delay of 0.1 seconds between each character
time.sleep(2)  # Wait for 2 seconds

pyautogui.press("enter")  # Press the Enter key
time.sleep(2)  # Wait for 2 seconds
pyautogui.press("tab")  # Press the Tab key to select Chrome
pyautogui.press("tab")  # Press the Tab key to select Chrome
pyautogui.press("tab")  # Press the Tab key to select Chrome
pyautogui.press("tab")  # Press the Tab key to select Chrome
pyautogui.press("tab")  # Press the Tab key to select Chrome
pyautogui.press("tab")  # Press the Tab key to select Chrome
pyautogui.press("tab")  # Press the Tab key to select Chrome
pyautogui.press("tab")  # Press the Tab key to select Chrome
pyautogui.press("tab")  # Press the Tab key to select Chrome
pyautogui.press("tab")  # Press the Tab key to select Chrome


pyautogui.press("enter")  # Press the Enter key
time.sleep(3)  # Wait for 3 seconds for Chrome to open
pyautogui.hotkey('ctrl', 't')  # Press Ctrl+T to open a new tab
pyautogui.typewrite("Bimeducation.in", interval=0.1)  # Type "Bimeducation.in" with a delay of 0.1 seconds between each character
pyautogui.press("enter")  # Press the Enter key
time.sleep(3)  # Wait for 3 seconds for the website to load
pyautogui.scroll(-500)  # Scroll down 500 units
time.sleep(1)  # Wait for 1 second
pyautogui.hotkey('ctrl', 'a')  # Press Ctrl+A to select all text
time.sleep(1)  # Wait for 1 second
pyautogui.hotkey('ctrl', 'c')  # Press Ctrl+C to copy

pyautogui.press("win")  # Press the Windows key
time.sleep(1)  # Wait for 1 second
pyautogui.typewrite("Notepad", interval=0.1)  # Type "Notepad" with a delay of 0.1 seconds between each character
time.sleep(1)  # Wait for 1 second
pyautogui.press("enter")  # Press the Enter key
time.sleep(1)  # Wait for 1 second
pyautogui.hotkey('ctrl', 'n')  # Press Ctrl+N to create a new file
time.sleep(1)  # Wait for 1 second
pyautogui.hotkey('ctrl', 'v')  # Press Ctrl+V to paste the copied text

screenshot = pyautogui.screenshot()  # Capture a screenshot of the entire screen
screenshot.save("test.png")  # Save the screenshot as "screenshot.png"

"""

#Playwright Automation
'''
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Launch a Chromium browser
    page = browser.new_page()  # Create a new page
    page.goto("https://www.bimeducation.in/")  # Navigate to the website
    time.sleep(30)  # Wait for 3 seconds for the website to load
    #page.screenshot(path="screenshot.png")  # Capture a screenshot of the page and save it as "screenshot.png"
    #browser.close()  # Close the browser
'''

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Launch a Chromium browser
    page = browser.new_page()  # Create a new page
    page.goto("https://www.bimeducation.in/")  # Navigate to the website
    page.wait_for_load_state("networkidle")  # Wait for the page to load completely
    time.sleep(30)  # Wait for 3 seconds for the website to load
    page.close()  # Close the browser