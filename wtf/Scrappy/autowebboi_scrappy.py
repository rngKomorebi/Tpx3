from webbot import Browser
import time
import pyautogui
import os
from selenium import webdriver

import numpy as np
import matplotlib.pyplot as plt

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

shot = input("Cislo vyboje:")
try:
    os.mkdir(shot)
except Exception:
    pass

os.chdir(shot)

# web = Browser()

# web.start_client()
# web.start_session()
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s' % (shot)}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=chrome_options)
driver.get('https://webcdb.tok.ipp.cas.cz/data_signals/728/%s/data?variant=&revision=1&downsample=100' % (shot))
# web.go_to("https://webcdb.tok.ipp.cas.cz")
# web.go_to("https://webcdb.tok.ipp.cas.cz/records/20055")
# web.go_to('https://webcdb.tok.ipp.cas.cz/data_signals/728/%s/data?variant=&revision=1&downsample=100' % (shot)) 

# web.get_current_window_handle()

time.sleep(2.5)

# web.type('kulkov', into='Username')
# web.press(web.Key.SHIFT + 'KULKOV')
pyautogui.typewrite('kulkov')
pyautogui.typewrite('\t')
pyautogui.typewrite('nejakejTenVUL168')
# web.press(web.Key.TAB)
# web.type('nejakejTenVUL168', into='Password')
pyautogui.typewrite('\t')
pyautogui.typewrite('\t')
pyautogui.typewrite('\r')

driver.quit()