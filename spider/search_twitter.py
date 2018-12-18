#coding=utf-8
import requests
from selenium import webdriver
import time
from  PIL import Image
from selenium.webdriver.common.action_chains import ActionChains
import os


def get_element_snapshot(element):
    #将页面滑动到当前位置处
    ActionChains(driver).move_to_element(element).perform()
    # 保存当前结果页面
    driver.save_screenshot("./temp.png")

    # 保存element的截图
    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']

    print(left,top,right,bottom)
    im = Image.open("./temp.png")
    im = im.crop((left - 5, top - 5, right + 5, bottom + 5))
    im.save('./tweet.png')
    #os.remove("./temp.png")
    return im

def get_latest_tweets_from_spic_user(user_id, last_tweet_time = None):
    driver.get("https://twitter.com/{}".format(user_id))
    #driver.switch_to.frame()
    time.sleep(10)
    return_tweets = {}
    stream = driver.find_element_by_css_selector("[class='stream']")
    timeline = stream.find_elements_by_css_selector('.tweet')
    for i in range(len(timeline)):
        tweet = {}
        print(i)
        is_retweet = False
        if 1 == len(timeline[i].find_elements_by_class_name('js-retweet-text')):
            is_retweet = True
        text = timeline[i].find_elements_by_class_name('js-tweet-text-container')[0].text
        tweet_snapshot = get_element_snapshot(timeline[i])
        tweet['is_retweet'] = is_retweet
        tweet['text'] = text

        print(is_retweet)
        print(text)





if __name__ == '__main__':
    ###  初始设置 ####
    # 实例化浏览器
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 静默模式
    driver = webdriver.Chrome('C:\ProgramData\Anaconda3\Scripts\chromedriver.exe',options=option)

    # 设置窗口大小
    driver.set_window_size(960, 1080)
    # 最大化窗口
    # driver.maximize_window()

    get_latest_tweets_from_spic_user('realDonaldTrump')

    # # 发送请求
    # driver.get('https://www.baidu.com/')
    #
    # # .page_source是获取网页的全部html
    # #print(driver.page_source)
    #
    # # 进行页面截屏
    # driver.save_screenshot("./baidu.jpg")
    #
    #
    # # 网页元素定位,输入关键词并搜索
    # driver.find_element_by_id('kw').send_keys('Python深度学习 pdf')
    # driver.find_element_by_id('su').click()
    # time.sleep(5)
    #
    # # 当前搜索结果页面的链接
    # print("current_url: ",driver.current_url)
    #
    # # 保存搜索结果页面
    # driver.save_screenshot("./搜索结果.jpg")
    #
    # # 保存第一条结果的截图
    # first_result = driver.find_element_by_id('1')
    # left = first_result.location['x']
    # top = first_result.location['y']
    # right = first_result.location['x'] + first_result.size['width']
    # bottom = first_result.location['y'] + first_result.size['height']
    #
    # im = Image.open("./搜索结果.jpg")
    # im = im.crop((left - 5, top - 5, right + 5 , bottom + 5))
    # im.save('./第一条搜素结果.png')


    # driver获取cookie
    # cookies = driver.get_cookies()
    # print(cookies)
    # print("*"*100)
    # cookies = {i["name"]:i["value"] for i in cookies}
    # print(cookies)


    # 退出浏览器
    driver.quit()


