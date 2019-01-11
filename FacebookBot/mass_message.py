import config as cf
import time
import re

friend_lists_url = 'https://www.facebook.com/mike.hoang.505/friends'
regex = '^https://www.facebook.com/.*?fref=pb&hc_location=friends_tab$'
unused_str = 'fref=pb&hc_location=friends_tab'


def run():
    cf.login()
    cf.driver.get(friend_lists_url)

    for i in range(0, 10):
        cf.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    friend_arr = []
    for i in range(1, 6):
        friends_list = cf.driver.find_element_by_xpath(
            '//*[@id="pagelet_timeline_app_collection_100013172746042:2356318349:2"]/ul[' + str(i) + ']')
        friends = friends_list.find_elements_by_tag_name("a")

        for f in friends:
            url = f.get_attribute('href')
            if(re.match(regex, url)):
                friend_id = url.split('https://www.facebook.com/')[1]
                if 'profile.php?' not in friend_id:
                    friend_id = friend_id.split(
                        '?' + unused_str)[0]
                else:
                    friend_id = friend_id.split(
                        'profile.php?id=')[1].split('&' + unused_str)[0]
                if friend_id not in friend_arr:
                    friend_arr.append(friend_id)

    for f in friend_arr:
        cf.send_message(f)


if __name__ == '__main__':
    run()
