# -*- coding:utf-8 -*-
import HtmlInput
import HtmlOutput
import HtmlDownloader
import HtmlDeal
import time
import os
import csv
import sys
import url2io
import json
import urllib2
from FileCompare import FileDiff

ErrorFile = "error.txt"#请手动清除
OutputFile = "result.json"
UrlFile = "id_url_new.csv"
ReUrlFile = 'OutputUrl.csv'

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

def Spider3(SpiderFile, FpError, FpOutput):
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
            OutputContent.TestSet(out_pots, int(IdList[i]), FpOutput)


def HtmlParser(paser_url, FpError):
    Downloader = HtmlDownloader.Downloader()
    SimpleDeal = HtmlDeal.SimpleDeal()
    OutputContent = HtmlOutput.OutputContent()
    html_text = Downloader.StaticDownloadOne(paser_url, FpError)
    if html_text == None:
        print "the url:%s is not exist\n" %(paser_url)
    else:
        plot_pots = SimpleDeal.Method2(paser_url,html_text,FpError)
        OutputContent.OutPlot(plot_pots)

def LocalHtmlParser(paser_url, FpError):
    Downloader = HtmlDownloader.Downloader()
    SimpleDeal = HtmlDeal.SimpleDeal()
    OutputContent = HtmlOutput.OutputContent()
    html_text = open(paser_url, 'r')
    print html_text
    if html_text == None:
        print "the url:%s is not exist\n" %(paser_url)
    else:
        plot_pots = SimpleDeal.Method2(paser_url,html_text,FpError)
        OutputContent.OutPlot(plot_pots)


#choose model
model_list = ["test plot model(1)",
"product model(2)",
"new feature model(3)",
"test the extract method(4)",
"test url2io API(5)",
"new product model(6)"]
print "-----The following model is:-----"
for i in model_list:
    print i

#model = raw_input("choose the model num:")
model = 6

if int(model) == 1:
    FpError = open(ErrorFile, 'a')
    FpError.write("start:\t" + time.ctime() + "\n\n")

    paser_url = 'http://money.163.com/15/0521/05/AQ46OS1Q00253B0H.html'
    HtmlParser(paser_url, FpError)

    FpError.write("stop:\t"+time.ctime()+"\n\n")
    FpError.close()

    

elif int(model) == 2:
    # 第一次爬取Url
    if os.path.exists(ReUrlFile):
        os.remove(ReUrlFile)#删除上一次重新爬取的链接
    else:
        pass
    FpError = open(ErrorFile, 'a')
    FpError.write("start:\t" + time.ctime() + "\n\n")
    FpOutput = open(OutputFile, 'w')


    Spider1(UrlFile, FpError, FpOutput)
    if os.path.exists(ReUrlFile):
        # 重新爬取Url，针对无法爬取的url
        FpError.write("-----Respider-----\n")
        print '-----respider-----\n'
        Spider1(ReUrlFile, FpError, FpOutput)
    else:
        print 'No Connection aborted part'

    FpError.write("stop:\t"+time.ctime()+"\n\n")
    FpError.close()
    FpOutput.close()


elif int(model)  == 3:
    if os.path.exists(ReUrlFile):
        os.remove(ReUrlFile)#删除上一次重新爬取的链接
    else:
        pass
    FpError = open(ErrorFile, 'a')
    FpError.write("start:\t" + time.ctime() + "\n\n")
    FpOutput = open(OutputFile, 'w')

    Spider2(UrlFile, FpError, FpOutput)
    if os.path.exists(ReUrlFile):
        # 重新爬取Url，针对无法爬取的url
        FpError.write("-----Respider-----\n")
        print '-----respider-----\n'
        Spider2(ReUrlFile, FpError, FpOutput)
    else:
        print 'No Connection aborted part'

    FpError.write("stop:\t"+time.ctime()+"\n\n")
    FpError.close()
    FpOutput.close()

elif int(model) == 4:
    if os.path.exists(ReUrlFile):
        os.remove(ReUrlFile)#删除上一次重新爬取的链接
    else:
        pass
    FpError = open(ErrorFile, 'a')
    FpError.write("start:\t" + time.ctime() + "\n\n")
    FpOutput = 'trans'

    TestFile = os.path.join(sys.path[0], "testset", "nju.csv")
    print TestFile
    Spider3(TestFile, FpError, FpOutput)
    if os.path.exists(ReUrlFile):
        # 重新爬取Url，针对无法爬取的url
        FpError.write("-----Respider-----\n")
        print '-----respider-----\n'
        Spider3(ReUrlFile, FpError, FpOutput)
    else:
        print 'No Connection aborted part'

    FpError.write("stop:\t"+time.ctime()+"\n\n")
    FpError.close()

elif int(model) == 5:
    api = url2io.API("6WBCZCoVRSiIzyph80Vexw")
    TestFile = os.path.join(sys.path[0], "testset", "nju.csv")
    out = "APItrans"
    print TestFile
    InputUrl = HtmlInput.InputUrl()
    IdList = InputUrl.ReadId(TestFile)
    UrlList = InputUrl.ReadUrl(TestFile)

    num = len(UrlList)

    for i in range(num):
        #print UrlList[i]
        ret = api.article(url=UrlList[i],fields=['text'])
        file1 = os.path.join(sys.path[0],"testset",IdList[i]+'.txt')
        file2 = os.path.join(sys.path[0],"testset",out+str(int(IdList[i]))+".txt")
        FpOutput = open(file2,'w')
        FpOutput.write(ret['text'].encode('utf-8'))
        FpOutput.close()
        simlarity = FileDiff().TwoFileSimilarity(file1, file2)
        print "of the file:"+IdList[i]+"\tTwoFileSimlarity\t"+str(simlarity)
        #print json.dumps(ret,indent=4,ensure_ascii=False).encode('utf-8')
        #print ret['text'].encode("utf-8")

elif int(model) == 6:
    print time.ctime()
    print "-----start----"
    start = time.time()
    refail_num = 0
    fail_num = 0
    permission_error = 0
    http_error = 0
    url_error = 0
    type_error = 0
    unknow_error = 0
    if os.path.exists(ReUrlFile):
        os.remove(ReUrlFile)#删除上一次重新爬取的链接
    else:
        pass

    file_404 = "record_404.csv"
    api = url2io.API("6WBCZCoVRSiIzyph80Vexw")
    InputUrl = HtmlInput.InputUrl()
    OutputContent = HtmlOutput.OutputContent()
    IdList = InputUrl.ReadId(UrlFile)
    UrlList = InputUrl.ReadUrl(UrlFile)
    FpOutput = open(OutputFile, 'w')
    num = len(UrlList)
    csvfile = open(ReUrlFile,'w')
    csvfile_404 = open(file_404,'w')


    for i in range(num):
        try:
            ret = api.article(url=UrlList[i], fields=['text','url','title'])
        except Exception as e:
            print e
            spamwriter = csv.writer(csvfile, quotechar=',', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([IdList[i], UrlList[i]])
            continue
        time.sleep(0)
       # print ("id:%d \t\t url:%s") % (int(IdList[i]), UrlList[i])
        if ret.has_key("error"):
            #req = urllib2.urlopen(UrlList[i])
            #url_trans = req.geturl()
            fail_num = fail_num + 1
            print ("id:%d \t\t url:%s") % (int(IdList[i]), UrlList[i])
            print ret
            if ret["error"] == "HTTPError":
                http_error = http_error + 1
                if ret["code"] == 404:
                    writer_404 = csv.writer(csvfile_404, quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    writer_404.writerow([IdList[i], UrlList[i]])
                elif ret["code"] == 599:
                    spamwriter = csv.writer(csvfile, quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow([IdList[i], UrlList[i]])
                else:
                    print "an unsolved error"
            elif ret["error"] == "PermissionError":
                permission_error = permission_error + 1
            elif ret["error"] == "URLError":
                url_error = url_error + 1
            elif ret["error"] == "TypeError":
                type_error = type_error + 1
            elif ret["error"] == "UnknownError":
                unknow_error = unknow_error + 1
            else :
                print "an unrecord error"
        else:
            #print ("id:%d \t\t url:%s") % (int(IdList[i]), UrlList[i])
            OutputContent.OutputEs(ret,IdList[i],FpOutput)
    csvfile.close()
    csvfile_404.close()

    if os.path.exists(ReUrlFile):
        # 重新爬取Url，针对无法爬取的url
        print '-----respider-----\n'
        ReUrlList = InputUrl.ReadUrl(ReUrlFile)
        ReIdList = InputUrl.ReadId(ReUrlFile)
        num = len(ReIdList)
        for i in range(num):
            time.sleep(10)
            try:
                ret = api.article(url=ReUrlList[i], fields=['text','url','title'])
                if ret.has_key("error"):
                    refail_num = refail_num + 1
                    print ("id:%d \t\t url:%s") % (int(ReIdList[i]), ReUrlList[i])
                    print ret
                else:
                    OutputContent.OutputEs(ret,ReIdList[i],FpOutput)
                    #print ("id:%d \t\t url:%s") % (int(ReIdList[i]), ReUrlList[i])
            except Exception as e:
                print e
                continue
    stop = time.time()
    print "\n\nhave use time:\t%f"%(stop-start)
    print "first fail num:\t%d"%(fail_num)
    print "HTTPError:\t%d"%(http_error)
    print "URLError:\t%d"%(url_error)
    print "UnknowError\t%d"%(unknow_error)
    print "PermissionError\t%d"%(permission_error)
    print "TypeError:\t%d"%(type_error)
    print "respider and fial num:\t%d"%(refail_num)

if int(model)==7:
    api = url2io.API("6WBCZCoVRSiIzyph80Vexw")
    url = "http://stuex.nju.edu.cn/a/www.hec.fr"
    ret = api.article(url=url, fields=['text','url','title'])
    print ret

