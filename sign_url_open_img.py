#coding=utf-8
#通过验证码图片地址直接打开图片
import urllib2,cStringIO
from PIL import Image
def open_img(url='验证码图片地址'):

    file=urllib2.urlopen(url)
    tmpIm=cStringIO.StringIO(file.read())
    im=Image.open(tmpIm)
    im.show()

if __name__=="__main__":
    url="http://console.xhj.com/admin/validateCode"
    open_img(url)
