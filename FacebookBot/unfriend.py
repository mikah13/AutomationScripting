import config as cf
import time
from selenium.webdriver.common.action_chains import ActionChains


def run():
    cf.login()
    time.sleep(1)
    cf.driver.get('https://www.facebook.com/blackjackhuy')
    time.sleep(.5)
    friend_button = cf.driver.find_element_by_class_name(
        'FriendButton')
    hover = ActionChains(cf.driver).move_to_element(friend_button)
    hover.perform()
    time.sleep(.3)
    unfriend_button = cf.driver.find_element_by_class_name('FriendListUnfriend')
    unfriend_button.click()
    time.sleep(2)


if __name__ == '__main__':
    run()
