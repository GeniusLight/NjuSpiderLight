# -*- coding:utf-8 -*-
import HtmlInput
import HtmlOutput
import HtmlDownloader
import HtmlDeal
import time


UrlFile = "id_url.csv"
ErrorFile = "error.txt"
OutputFile = "result.json"
InputUrl = HtmlInput.InputUrl()
IdList = InputUrl.ReadId(UrlFile)
UrlList = InputUrl.ReadUrl(UrlFile)
num = len(UrlList)

FpError = open(ErrorFile, 'a')
FpError.write("start:\t"+time.ctime()+"\n\n")
FpOutput = open(OutputFile, 'w')
Downloader = HtmlDownloader.Downloader()
SimpleDeal = HtmlDeal.SimpleDeal()
OutputContent = HtmlOutput.OutputContent()
for i in range(num):
    print ("id:%d \t\t url:%s") % (int(IdList[i]), UrlList[i])
    html_text = Downloader.StaticDownload(UrlList[i], FpError)
    OutputS = SimpleDeal.Method1(UrlList[i], html_text, FpError)
    OutputContent.OutputEs(OutputS, int(IdList[i]), FpOutput)

FpError.write("stop:\t"+time.ctime()+"\n\n")
FpError.close()
FpOutput.close()
