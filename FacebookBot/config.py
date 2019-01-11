from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key, Controller
from message import msg
from numbers import Number
url = 'https://www.facebook.com/'
username = 'anhminhhoang138@gmail.com'
password = 'cunbong0812'

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


def unfriend(id):
    driver.get('https://www.facebook.com/' + id)
    time.sleep(.5)
    friend_button = driver.find_element_by_class_name(
        'FriendButton')
    hover = ActionChains(driver).move_to_element(friend_button)
    hover.perform()
    time.sleep(.3)
    unfriend_button = cf.driver.find_element_by_class_name(
        'FriendListUnfriend')
    unfriend_button.click()
    time.sleep(2)
