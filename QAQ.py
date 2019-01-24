from tkinter import *
import requests
from bs4 import BeautifulSoup
import re
import sys,os
#纯内部测试玩耍小程序
#异常未处理
#代码未规范
#界面未美化
#BUG多多
root = Tk()
root.title("爬取的url可以直接浏览器观看，可迅雷下载")
root.resizable(width=False,height=False)
var_l = StringVar()
var_u = StringVar()
var_l.set('7000')
var_u.set('7000')
e_l = Entry(root,textvariable=var_l)
e_u = Entry(root,textvariable=var_u)
e_l.pack()
e_u.pack()
BASE_URL_NAME = 'qipa22'
base_url = 'https://www.' + BASE_URL_NAME + '.com/video/'
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
def get_url (video_num):
    url = base_url + repr(video_num)
    return url

def get_video_url():
    VIDEO_LO_LIMIT = int(e_l.get())
    VIDEO_UP_LIMIT = int(e_u.get())
    video_limit = [VIDEO_LO_LIMIT, VIDEO_UP_LIMIT]
    for video_num in range(video_limit[0],video_limit[1]+1):
        url = get_url(video_num)
        print("视频号："+repr(video_num))
        print("--------目标视频网址"+' '+url)
        try:
            requesone = requests.get(url, headers=headers)
            html = requesone.text
            soup = BeautifulSoup(html, 'lxml')
            title = soup.title.string  # 获取title
            url_d = str(soup.find('source').attrs['src'])
            want_title = re.match('.*\s', str(title)).group().replace(' ', '')
            # print('--------目标视频的标题' + title)
            print('--------标题--' + want_title + ' 地址 ' + url_d)
            cu_path = os.path.dirname(os.path.dirname(sys.argv[0]))
            c_path = str(cu_path).replace('\\','/') + '/url/'
            print(os.path.exists(c_path))
            print(c_path)
            if not os.path.exists(c_path):
                os.makedirs(c_path)
            path = c_path+ repr(video_limit[0]) + '-' + repr(video_limit[1]) + '.txt'
            print("保存路径"+path)
            with open(path, 'a') as file:
                file.write(want_title)
                file.write(url_d + '\n')
                print("保存下载地址成功")
                print("爬取成功")
        except AttributeError as e:
            print(e)

def run():
    get_video_url()

def exi():
    sys.exit()

button1 = Button(root,text="开始爬取",command=run)
button2 = Button(root,text='关闭',command=exi)
button1.pack()
button2.pack()
root.mainloop()