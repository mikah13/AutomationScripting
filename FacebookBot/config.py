from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key, Controller
import msg from message

url = 'https://www.facebook.com/'
username = ''
password = ''

chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}

chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(
    executable_path="./chromedriver", chrome_options=chrome_options)


def login():
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
    time.sleep(.3)


def send_message(id):
    messenger = 'https://www.facebook.com/messages/t/' + id
    driver.get(messenger)
    driver.find_element_by_xpath("//*[@data-editor]").click()
    actions = ActionChains(driver)
    actions.send_keys(msg)
    actions.perform()
    keyboard = Controller()
    keyboard.press(Key.enter)
    time.sleep(.3)
