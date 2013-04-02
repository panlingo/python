#!/usr/bin/env python
#coding=utf-8

from os.path import basename, isdir, abspath, isfile, splitext, normpath
from os import listdir
from PIL import Image

d = 'E:/git/zhuxuehuang/python/module_code'
imgs = ('.jpg', '.jpeg', '.gif', '.png')

def eachdir(path, depth=0):
    if isfile(path):
        print depth *  '    ' + '|_', basename(path), ' *do'
        absfile = normpath(abspath(path))
        #可以写图像缩略图代码
        fname, fext = splitext(absfile)
        if fext in imgs:
            #print('Img')
            im = Image.open(absfile)
            im.thumbnail((100, 100), Image.ANTIALIAS)
            im.save(fname+'_thumb'+fext)
    else:
        print depth *  '    ' + '|_', basename(path)
    if(isdir(path)):
        for item in listdir(path):
            eachdir(path+'/'+item, depth+1)

if __name__ == '__main__':
    eachdir(d)
