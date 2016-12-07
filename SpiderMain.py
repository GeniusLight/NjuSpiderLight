# -*- coding:utf-8 -*-
import HtmlInput
import HtmlOutput
import HtmlDownloader
import HtmlDeal
import time
import os


def SpiderMain(SpiderFile, FpError, FpOutput):
    Downloader = HtmlDownloader.Downloader()
    SimpleDeal = HtmlDeal.SimpleDeal()
    OutputContent = HtmlOutput.OutputContent()
    InputUrl = HtmlInput.InputUrl()
    IdList = InputUrl.ReadId(SpiderFile)
    UrlList = InputUrl.ReadUrl(SpiderFile)
    num = len(UrlList)

    for i in range(num):
        print ("id:%d \t\t url:%s") % (int(IdList[i]), UrlList[i])
        html_text = Downloader.StaticDownload(UrlList[i], int(IdList[i]), FpError)
        if html_text == None:
            pass
        else:
            OutputS = SimpleDeal.Method1(UrlList[i], html_text, FpError)
            OutputContent.OutputEs(OutputS, int(IdList[i]), FpOutput)


ErrorFile = "error.txt"#请手动清除
OutputFile = "result.json"
UrlFile = "id_url.csv"
ReUrlFile = 'OutputUrl.csv'

if os.path.exists(ReUrlFile):
    os.remove(ReUrlFile)#删除上一次重新爬取的链接
else:
    pass

FpError = open(ErrorFile, 'a')
FpError.write("start:\t" + time.ctime() + "\n\n")
FpOutput = open(OutputFile, 'w')

# 第一次爬取Url
SpiderMain(UrlFile, FpError, FpOutput)

if os.path.exists(ReUrlFile):
    # 重新爬取Url，针对无法爬取的url
    FpError.write("-----Respider-----\n")
    print '-----respider-----\n'
    SpiderMain(ReUrlFile, FpError, FpOutput)
else:
    print 'No Connection aborted part'

FpError.write("stop:\t"+time.ctime()+"\n\n")
FpError.close()
FpOutput.close()
