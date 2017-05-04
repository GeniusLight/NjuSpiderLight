# -*- coding:utf-8 -*-
import HtmlInput
import HtmlOutput
import HtmlDownloader
import HtmlDeal
import time
import os


def Spider1(SpiderFile, FpError, FpOutput):
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


def Spider2(SpiderFile, FpError, FpOutput):
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
            out_pots = SimpleDeal.Method3(UrlList[i], html_text, FpError)
            OutputContent.OutputEsNew(out_pots, int(IdList[i]), FpOutput)


def HtmlParser(paser_url, FpError):
    Downloader = HtmlDownloader.Downloader()
    SimpleDeal = HtmlDeal.SimpleDeal()
    OutputContent = HtmlOutput.OutputContent()
    html_text = Downloader.StaticDownloadOne(paser_url, FpError)
    if html_text == None:
        print "the url:%s is not exist\n" %(url)
    else:
        plot_pots = SimpleDeal.Method2(paser_url,html_text,FpError)
    OutputContent.OutPlot(plot_pots)


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


#choose model
model_list = ["test model(1)","product model(2)","new feature model(3)"]
print "-----The following model is:-----"
for i in model_list:
    print i

model = raw_input("choose the model num:")

if int(model) == 1:
    paser_url = 'http://stuex.nju.edu.cn/a/xzzx/2015/0727/165.html'
    HtmlParser(paser_url, FpError)

    

elif int(model) == 2:
    # 第一次爬取Url
    Spider1(UrlFile, FpError, FpOutput)
    if os.path.exists(ReUrlFile):
        # 重新爬取Url，针对无法爬取的url
        FpError.write("-----Respider-----\n")
        print '-----respider-----\n'
        Spider1(ReUrlFile, FpError, FpOutput)
    else:
        print 'No Connection aborted part'

elif int(model)  == 3:
    Spider2(UrlFile, FpError, FpOutput)
    if os.path.exists(ReUrlFile):
        # 重新爬取Url，针对无法爬取的url
        FpError.write("-----Respider-----\n")
        print '-----respider-----\n'
        Spider2(ReUrlFile, FpError, FpOutput)
    else:
        print 'No Connection aborted part'

else:
    print "The no exist model\n"


FpError.write("stop:\t"+time.ctime()+"\n\n")
FpError.close()
FpOutput.close()
