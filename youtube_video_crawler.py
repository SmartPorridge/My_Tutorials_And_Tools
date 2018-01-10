# coding:utf-8
import os
import re
import urllib2


def getHtml(url):
    print url
    page = urllib2.urlopen(url)
    html = page.read()
    return html


def getUrl(html, video_url_list):
    reg = r"(?<=a\shref=\"/watch).+?(?=\")"
    urlre = re.compile(reg)
    urllist = re.findall(urlre, html)
    format = "https://www.youtube.com/watch%s\n"
    #f = open("\output.txt", 'a')
    for url in urllist:
        result = (format % url)
        #f.write(result)
        print result
        video_url_list.append(result)
    #f.close()


root = 'D:/VideoDatasets/zhian_fight/'
video_path = 'crawle_get_video/'

pages = 20
#search_words = ['斗殴+监控','监控实拍+打架','surveillance+fight']
#search_words = ['city+riots+CCTV']
#search_words = ['demonstration+clash']
search_words = ['Fighting+and+brawling+in+surveillance']

video_list = []
video_folder_list = os.listdir(root + video_path)
for folder in video_folder_list:
    videos_in_folder = os.listdir(root + video_path +'/'+folder)
    for video in videos_in_folder:
        video_list.append(video.split('.')[0])

f = open(root+'crawle_get_video.txt', 'a')
#f.write('sss')
f.flush()

for key_word in search_words:
    for i in range(1, pages):
        print "parsing page {}".format(i)
        html = getHtml("https://www.youtube.com/results?sp=EgIYAQ%253D%253D&search_query={}&page={}".format(key_word, i))
        #print html
        video_url_list = []
        getUrl(html, video_url_list)
        for video_url in video_url_list:
            video_url = video_url.strip()
            f.write(video_url+'\n')
            f.flush()
            video_name = video_url.split('v=')[1]
            print video_name
            print root+'youtube-dl.exe -f best -f mp4 {} -o {}.mp4'.format(video_url,root+video_name)
            if video_name not in video_list:
                os.system('{0}youtube-dl.exe -f best -f mp4 {1} -o {0}{2}{3}/{4}.mp4'.format(root,video_url,video_path,key_word,video_name))
print "done"
