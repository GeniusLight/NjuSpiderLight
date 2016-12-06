# -*- coding:utf-8 -*-
import HtmlInput
import HtmlOutput
import HtmlDownloader
import HtmlDeal
import time
import os


def SpiderMain(Urlfile, FpError, FpOutput):
    Downloader = HtmlDownloader.Downloader()
    SimpleDeal = HtmlDeal.SimpleDeal()
    OutputContent = HtmlOutput.OutputContent()
    InputUrl = HtmlInput.InputUrl()
    IdList = InputUrl.ReadId(UrlFile)
    UrlList = InputUrl.ReadUrl(UrlFile)
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

os.remove(ReUrlFile)#删除上一次遗留的链接
FpError = open(ErrorFile, 'a')
FpError.write("start:\t" + time.ctime() + "\n\n")
FpOutput = open(OutputFile, 'w')

# 第一次爬取Url
SpiderMain(UrlFile, FpError, FpOutput)

#重新爬取Url，针对无法爬取的url
FpError.write("-----Respider-----\n")
print '-----respider-----\n'
SpiderMain(ReUrlFile, FpError, FpOutput)

FpError.write("stop:\t"+time.ctime()+"\n\n")
FpError.close()
FpOutput.close()
