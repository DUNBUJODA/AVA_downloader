# coding= UTF-8

# Take a look at README first
#
# Author: Fing @EI, WHU
# Finish on 2016-11-13
#
# Usage:
#    $python ava_downloader.py beginIndex endIndex
#  
#  Also you can download in multi-process.
#
# Make sure AVA.txt and folder 'image' is under the directory 
# Note: few images may be deleted from the website
#

import logging
from urllib.error import HTTPError
from urllib import request
import re
import sys
import os
from fake_useragent import UserAgent   

# 下载：pip install fake-useragent 
# https://blog.csdn.net/ITBigGod/article/details/103248172


ua = UserAgent()

# 请求
# url = 'https://www.baidu.com/'
# response = requests.get(url, headers=headers)
# print(response.status_code)


# 得到HTML文档,路径为url
def getHtml(url):
    """Get HTML data from url"""
    # headers = {'User-Agent', ua.random}    # 伪装
    headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36")

    #这是代理IP
    proxy = {'http':'115.221.244.197:9999'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [headers]
    #安装OPener
    request.install_opener(opener)
    try:
        #使用自己安装好的Opener
        response = request.urlopen(url)
        #读取相应信息并解码
        html = response.read().decode("utf-8", "ignore")
        return html
    except HTTPError as e:
        logging.error(f"Download failed for {url}. Error Message: {e.msg}")
        return None


# 回调函数 显示下载进度
def schedule(a, b, c):
    '''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


# 正则匹配图片并用URLRetrieve下载
def getImg(html, imageID, imageIndex):
    # reg = r'http.*?' + imageID + r'\.jpg'
    reg = r'images\.dpchallenge\.com\/.*?' + imageID + r'\.jpg'
    # print(reg)
    imgre = re.compile(reg)  # 编译成正则表达式变量
    imglist = re.findall(imgre, html)
    # print(imglist)
    if len(imglist) > 0:
        for imgurl in imglist:
            print(imgurl, "-->", savePath, imageIndex, '.jpg')
            request.urlretrieve("http://" + imgurl, os.path.join(savePath, imageIndex + '.jpg'), schedule)
        return 1
    else:
        return 0

URLprefix = r'http://www.dpchallenge.com/image.php?IMAGE_ID='
AVAtxt = r'AVA_dataset/AVA.txt'
savePath = r'AVA_dataset/image/'


# 检查参数个数
if len(sys.argv) < 3:
    print ('arg error # python xxx.py beginIndex endIndex')
    exit()


# 必须>=1
beginIndex = int(sys.argv[1])
# 必须<= 255530
endIndex = int(sys.argv[2])


# 打开AVA.txt 获取图片路径
f = open(AVAtxt)
for line in f:
    line = line.strip().split(' ')
    imageIndex = line[0]  # 得到图片序号

    if int(imageIndex) < beginIndex:
        continue
    elif int(imageIndex) > endIndex:
        break

    # 跳过已存在的图片
    if os.path.isfile(os.path.join(savePath, imageIndex + '.jpg')) == True:
        continue

    # 得到图片网址
    imageID = line[1]
    URL = URLprefix + imageID
    html = getHtml(URL)
    
    if html == None:
        print('image%s failed. HTTPError.' % imageIndex)
        continue

    if getImg(html, imageID, imageIndex):
        print('image%s success' % imageIndex)
    else:
        print('image%s failed' % imageIndex)