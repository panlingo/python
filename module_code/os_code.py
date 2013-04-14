#!/usr/bin/env python
#coding=utf-8
#13-4-14 下午10:03

import os

l = os.listdir('.')
#print(l)

for i in l:
    #print(os.path.abspath(i))
    pass


for i in os.walk('/mnt/github.com/', topdown=False):
    print i


def VisitDir(path):
    for root,dirs,files in os.walk(path):
        for filespath in files:
            print os.path.join(root,filespath)
if __name__ == "__main__":
    path = "/mnt/github.com/"

VisitDir(path)