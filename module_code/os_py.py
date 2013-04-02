__author__ = 'zhuxh'

import os


d = 'E:/git/zhuxuehuang'

def each_dir(dir):
    if os.path.exists(dir):
        if os.path.isdir(dir):
            #print 'yes dir\n' + '=' * 10
            os.path.abspath()
            tmp = os.listdir(dir)
            for item in tmp:
                each_dir(item)
                print item;
        else:
            print('not dir')
    else:
        print('not path')

each_dir(d)