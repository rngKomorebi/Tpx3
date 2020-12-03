# =============================================================================
# Donwload data from the COMPASS database WebCDB. Start with a shot number,
# the code will go to the web, automatically log in and download the data:
# plasma current, HXR and neutrons from scintillators, SXR from AXUV diodes,
# gas puff
# =============================================================================
import time # for a pause
import pyautogui # automatic mouse and keyboard
import os # for folder manipulations
from selenium import webdriver # to get to the web
from selenium.webdriver.common.keys import Keys
import os.path
from path_to_shot import *
import numpy as np

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

shot = int(input("Shot number:"))

# Go to the @shot folder
try:
    path = path_to_shot(shot)
except:
    raise SystemExit

# Urls and datafiles: 1-current, 2-HXR, 3-SXR, 4-neutrons, 5-gas puff
url1 = 'https://webcdb.tok.ipp.cas.cz/data_signals/728/%s/data?variant=&revision=1&downsample=100' % (shot)
url2 = 'https://webcdb.tok.ipp.cas.cz/data_signals/1266/%s/data?variant=&revision=1&downsample=100' % (shot)
url3 = 'https://webcdb.tok.ipp.cas.cz/data_signals/1195/%s/data?variant=&revision=1&downsample=100' % (shot)
url4 = 'https://webcdb.tok.ipp.cas.cz/data_signals/2122/%s/data?variant=&revision=1&downsample=100' % (shot)
url5 = 'https://webcdb.tok.ipp.cas.cz/data_signals/4789/%s/data?variant=&revision=1' % (shot)

file1 = 'I_plasma_Rogowski_coil_RAW-%s.txt' % shot
file2 = 'hard_X_rays-%s.txt' % shot
file3 = 'SXR_A_1-%s.txt'% shot 
file4 = 'neutron_detection_scintillator-%s.txt' % shot
file5 = 'MARTE_NODE.FeedbackDataCollection.GasPuffAnalogueOutputSecondGasPuff-%s.txt' % shot

url_list = [url1, url2, url3, url4, url5]
file_list = [file1, file2, file3, file4, file5]
no_file_index_full = np.zeros(5)

# Change Chrome download folder to the current one @ shot
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : path}
chrome_options.add_experimental_option('prefs', prefs)

# Check, if the file exists. If no - go to the web, log in, download the file
j = 0
i = 0

for i in range (0, len(url_list)):
    if os.path.isfile(file_list[i]):
        print ("File %i exist" %i)
    else:
        no_file_index_full[j] = i
        j = j + 1
        
if j > 0:
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=chrome_options)
    driver.get('https://webcdb.tok.ipp.cas.cz/')
    time.sleep(2)
    pyautogui.typewrite('kulkov')
    pyautogui.typewrite('\t')
    pyautogui.typewrite('nejakejTenVUL168')
    pyautogui.typewrite('\t')
    pyautogui.typewrite('\t')
    pyautogui.typewrite('\r')
    ind = 0
    for i in range (0,j):
        ind = no_file_index_full[i].astype(int)
        url_present = url_list[ind]
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        driver.get(url_present)
    time.sleep(3)   
    driver.quit()
