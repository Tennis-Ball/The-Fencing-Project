from ast import Str
from optparse import Option
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui
import time
import re


driver = webdriver.Chrome("chromedriver.exe")
driver.set_window_size(1400, 1000)
driver.get("https://fencingtimelive.com/tournaments/search/advanced")
time.sleep(2)

for i in range(9):
    pyautogui.press("tab")
time.sleep(0.5)
pyautogui.press("tab")
for i in range(10):
    pyautogui.press("left")
driver.find_element(By.CLASS_NAME, "picker__day--infocus").click()

pyautogui.press("tab")
time.sleep(0.5)
pyautogui.press("enter")
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.press("enter")

time.sleep(4)
html = str(driver.page_source.encode("utf-8"))
IDs = re.findall('data-uniqueid="[A-Z0-9]*"', html)
print(len(IDs))

with open("FTL_unique_IDs.txt", "w") as f:
    for line in IDs:
        f.write(str(re.search('"[A-Z0-9]*', line).group())[1:] + "\n")
f.close()
quit()
