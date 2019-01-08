from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from message import msg
from pynput.keyboard import Key, Controller

url = 'https://www.facebook.com/'
username = 'anhminhhoang138@gmail.com'
password = 'cunbong0812'
messenger = 'https://www.facebook.com/messages/t/blackjackhuy '


def run():

    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}

    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path="./chromedriver", chrome_options=chrome_options)

    driver.get(url)

    driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

    time.sleep(.5)
    driver.get(messenger)
    driver.find_element_by_xpath("//*[@data-editor]").click()
    actions = ActionChains(driver)
    actions.send_keys(msg)
    actions.perform()
    keyboard = Controller()
    keyboard.press(Key.enter)
    time.sleep(1)


if __name__ == '__main__':
    run()
