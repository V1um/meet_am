email = ('EMAIL')  # skriv din email
username = ('BRUGERNAVN')  # skriv unilogin brugernavn
password = ('ADGANGSKODE')  # skriv password til unilogin
meetcode = ('MEET KODE HER')  # skriv googlemeet koden
textinchat = ('TEKSTEN DU VIL SKRIVE')
waittime = (120) # skriv hvor langtid der skal gå før den skriver i chat (1 = 1 sekundt) (default 120sekunder/2minutter)
data_log = ('C:\\Users\\Downloads\\meet_am\\data.log') # hvis du vil have data fra hver gang du joiner et meet og hvad du skriver så skriv destinationen til "data.log" (Det skal være \\ for at virke)


# ------------------------
# DONT TOUCH UNDER HERE!!!
# ------------------------
# ------------------------
# DONT TOUCH UNDER HERE!!!
# ------------------------
# ------------------------
# DONT TOUCH UNDER HERE!!!
# ------------------------


import sys
import selenium
import time
import math
import logging
from datetime import datetime
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
from random import shuffle
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

print("Loggged in succesfully")

opt = Options()

opt.add_argument("--disable-infobars")

opt.add_argument("start-maximized")

opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", {

    "profile.default_content_setting_values.media_stream_mic": 1,

    "profile.default_content_setting_values.media_stream_camera": 1,

    "profile.default_content_setting_values.geolocation": 1,

    "profile.default_content_setting_values.notifications": 1

})

delay = 3

url = "https://meet.google.com/landing?authuser"


driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver_path = driver


driver.get(url)

time.sleep(1)

email_textbox = driver.find_element_by_id("identifierId")
email_textbox.send_keys(email)
time.sleep(1)
email_textbox.send_keys(Keys.RETURN)

time.sleep(1)

username_textbox = driver.find_element_by_id("username")
username_textbox.send_keys(username)

time.sleep(1)
username_textbox.send_keys(Keys.RETURN)

password_textbox = driver.find_element_by_id("form-error")
password_textbox.send_keys(password)
time.sleep(1)
password_textbox.send_keys(Keys.RETURN)

#cmvVG
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb"))
    )
    element.click()

except:
    NoSuchElementException

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-fmcmS-wGMbrd"))
    )
    element.click()


except:
    NoSuchElementException

time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(meetcode)

time.sleep(1)
actions.send_keys(Keys.RETURN)
actions.perform()

time.sleep(3)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

time.sleep(1)
actions.key_down(Keys.CONTROL)
actions.send_keys("e")
time.sleep(1)
actions.send_keys("d")
actions.key_up(Keys.CONTROL)
actions.perform()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "NPEfkd"))
    )
    element.click()

except:
    NoSuchElementException

time.sleep(1)

webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

time.sleep(1)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "HKarue"))
    )
    element.click()

except:
    NoSuchElementException


logging.basicConfig(filename=data_log,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()

logger.info(username + " " + "joined" + " | " + "Du skrev:" + " " + textinchat)


print("Du er nu i meet: : %s" % driver.title)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Du er joinet klokken: =", current_time)

time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(textinchat)
time.sleep(waittime)
actions.send_keys(Keys.RETURN)
actions.perform()
