from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time

adblock_extension_path = 'adblock.crx'

# Create a new instance of the Chrome web driver and add the extension
options = webdriver.ChromeOptions()
options.add_extension(adblock_extension_path)

# Start Chrome with the ad-blocking extension
driver = webdriver.Chrome(options=options)

# Navigate to the website with the pages
driver.get("https://nowfashion.com/")
time.sleep(2)
pyautogui.hotkey('ctrl', 'w')
actions = ActionChains(driver)
time.sleep(1)
j = 0
for i in range(11):
    pyautogui.hotkey('tab')
while(True):

    time.sleep(1)
    actions.send_keys(Keys.TAB * j)
    actions.perform()
    time.sleep(2)
    current_elem = driver.switch_to.active_element.get_attribute('href')
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.get(current_elem)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(20)
    j = j + 3
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'j')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')


time.sleep(7)

# Close the web browser
driver.quit()
