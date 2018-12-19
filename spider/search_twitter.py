#coding=utf-8
from selenium import webdriver
import time,os
from urllib import request,parse
from  PIL import Image
from selenium.webdriver.common.action_chains import ActionChains
from translate import Translator
from googletrans import Translator as Google_Translator


def get_element_snapshot(element, pad = 0):
    # 保存当前结果页面
    driver.save_screenshot("./tmp/temp.png")

    # 保存element的截图
    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']

    #print(left, top, right, bottom)
    im = Image.open("./tmp/temp.png")
    im = im.crop((left - pad, top - pad, right + pad, bottom + pad))
    os.remove("./tmp/temp.png")
    return im

def get_tweet_snapshot(data_tweet_id, user_homepage):
    current_tweet_url = "{}/status/{}".format(user_homepage, data_tweet_id)
    driver.get(current_tweet_url)

    # 弹出的界面
    PermalinkOverlay_body = driver.find_element_by_class_name('PermalinkOverlay-body')
    # get focus tweet
    if len(PermalinkOverlay_body.find_elements_by_css_selector("[class = 'permalink-inner permalink-tweet-container']")):
        focus_tweet = PermalinkOverlay_body.find_element_by_css_selector("[class = 'permalink-inner permalink-tweet-container']")
    else:
        focus_tweet = PermalinkOverlay_body.find_element_by_css_selector("[class = 'permalink-inner permalink-tweet-container ThreadedConversation ThreadedConversation--permalinkTweetWithAncestors")

    # 获取element的截图
    focus_tweet_snapshot = get_element_snapshot(focus_tweet)
    focus_tweet_snapshot.save('./tmp/tweet_{}.png'.format(data_tweet_id))
    return focus_tweet_snapshot

def translate_google(src, dest='zh-CN'):
    translate = Google_Translator()
    return translate.translate(src,dest=dest)

def translate(src, dest='zh-CN'):
    translator = Translator(to_lang="chinese")
    translation = translator.translate(src)
    return translation

def get_latest_tweets_from_spic_user(user_id, last_data_tweet_id = None):
    user_homepage = "https://twitter.com/{}".format(user_id)
    driver.get(user_homepage)
    time.sleep(20)

    return_tweets = []
    stream = driver.find_element_by_css_selector("[class='stream']")
    timeline = stream.find_elements_by_css_selector('.tweet')
    for i in range(len(timeline)):
        #print(i)
        tweet = {}
        # get current tweet content
        is_retweet = False
        if len(timeline[i].find_elements_by_class_name('js-retweet-text')):
            is_retweet = True
        text = timeline[i].find_elements_by_class_name('js-tweet-text-container')[0].text
        data_tweet_id = timeline[i].get_attribute('data-tweet-id')

        tweet['data_tweet_id'] = data_tweet_id
        tweet['is_retweet'] = is_retweet
        tweet['text'] = text
        #print(tweet)
        return_tweets.append(tweet)

    # get every tweet's snapshot and translate text to Chinese
    for i in range(len(return_tweets)):
        data_tweet_id = return_tweets[i]['data_tweet_id']
        tweet_snapshot = get_tweet_snapshot(data_tweet_id, user_homepage)
        text_zh_CN = translate_google(return_tweets[i]['text']).text
        #text_zh_CN = translate(return_tweets[i]['text'])

        return_tweets[i]['tweet_snapshot'] = tweet_snapshot
        return_tweets[i]['text_zh_CN'] = text_zh_CN
        print(data_tweet_id)
        print(return_tweets[i]['text'])
        print(text_zh_CN)

    return return_tweets


if __name__ == '__main__':
    ###  setting ####
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # slient mode
    driver = webdriver.Chrome('C:\ProgramData\Anaconda3\Scripts\chromedriver.exe',options=option)

    # set broswer window size
    #driver.set_window_size(960, 1080)
    # maximize broswer window size
    # driver.maximize_window()

    #recent_tweets = get_latest_tweets_from_spic_user('realDonaldTrump')
    recent_tweets = get_latest_tweets_from_spic_user('nasa')
    #print(recent_tweets)
    for i,tweet in enumerate(recent_tweets):
        print('-------------')
        print(i)
        print("is_retweet: ",tweet['is_retweet'])
        print(tweet['text'])
        print(tweet['text_zh_CN'])

    # quit broswer
    driver.quit()


