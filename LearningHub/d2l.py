from selenium import webdriver
from selenium.webdriver.chrome.options import Options


import time

url = 'https://my.bcit.ca/cp/home/displaylogin'
username = 'A01020970'
password = 'Cunbong0812'


def run():

    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}

    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path="./chromedriver", chrome_options=chrome_options)

    driver.get(url)

    driver.find_element_by_xpath('//*[@id="user"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="login_btn"]').click()

    time.sleep(13)
    # driver.find_element_by_xpath('//*[@id="fbDockChatBuddylistNub"]/a').click()
    # driver.find_element_by_xpath('//*[@id="u_0_a"]/div[2]/div[2]').click()




    # driver.find_element_by_xpath(
    #     '//*[@id="js_1v"]/div/div/div[2]/div/div/div/div').send_keys('hello from python')
    # driver.find_element_by_xpath(
    #     '//*[@id="js_1h"]/div[2]/div[3]/div[2]/div/div/button').click()


if __name__ == '__main__':
    run()
