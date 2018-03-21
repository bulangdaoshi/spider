from urllib.request import urlopen,urlretrieve,Request
import re

def get_image(url):

    response = urlopen(url)
    data = response.read().decode('utf-8')
    string = r'src="(https://imgsa\.baidu\.com.*?\.jpg)" pic_ext="jpeg"'
    urls = re.findall(string, data)
    print(urls)
    x = 0
    for url in urls:
        print(url)
        urlretrieve(url,"{0}.jpg".format(x))
        x +=1

get_image("https://tieba.baidu.com/p/3797994694?red_tag=1448564092")
