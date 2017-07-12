# -*- coding:utf-8 -*-
import HtmlInput
import HtmlOutput
import HtmlDownloader
import HtmlDeal
import time
import os
import csv
import sys
import json
import urllib2
from FileCompare import FileDiff
import re

ErrorFile = "error.txt"#请手动清除
OutputFile = "result.json"
UrlFile = "id_url_new.csv"
ReUrlFile = 'OutputUrl.csv'

model_list = [
"test small set of url(0)",
"test big set of url(1)"
]
for model_item in model_list:
    print model_item

model_num = raw_input("Choose the model num:\n")

if int(model_num) == 0:
    InputUrl = HtmlInput.InputUrl()
    Downloader = HtmlDownloader.Downloader()
    SimpleDeal = HtmlDeal.SimpleDeal()

    FpError = open(ErrorFile, 'a')
    FpError.write("start:\t" + time.ctime() + "\n\n")

    id_list = InputUrl.ReadId(UrlFile)
    url_list = InputUrl.ReadUrl(UrlFile)
    num = len(url_list)
    test_url = "https://cs.nju.edu.cn/changxu/"

    for i in range(num):
        html_text = Downloader.StaticDownload(url_list[i], int(id_list[i]), FpError)
        #html_text = Downloader.StaticDownload(test_url, 0, FpError)
        if html_text == None:
            pass#需要进一步处理

        else:
            content = SimpleDeal.DeleteLabel(html_text)
            re_chinese = re.findall(u'[\u4e00-\u9fa5]',content)
            re_english = re.findall("[A-Za-z]+", content)
            print "english is :"
            print len(re_english)
            print "chinese is :"
            print len(re_chinese)
            break
