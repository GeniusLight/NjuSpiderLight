#coding:utf-8
import HtmlOutput
from numpy import arange
import HtmlDownloader
import HtmlDeal
import HtmlOutput
import HtmlInput
import InputUrl
import time
import os
import sys
from FileCompare import FileDiff


limit_len = [6]
limit_ratio = arange(0,1.0,0.01)
limit_num = range(0,10,1)
max_num = range(0,20,2)
opt_limit_len = 0
opt_limit_ratio = 0
opt_limit_num = 0
opt_max_num = 0
opt_similarity = 0

ParaRecord = "para.txt"
FpPara = open(ParaRecord,'a')
for limit_len in limit_len:
    for limit_ratio in limit_ratio:
        for limit_num in limit_num:
            for max_num in max_num:
                GetTrans(limit_len,limit_ratio,limit_num,max_num)

FpPara.close()


def Spider3(SpiderFile, FpError, FpOutput, limit_len, limit_ratio, limit_num, max_num):
    Downloader = HtmlDownloader.Downloader()
    SimpleDeal = HtmlDeal.SimpleDeal()
    OutputContent = HtmlOutput.OutputContent(limit_len, limit_ratio, limit_num, max_num)
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
            file1 = os.path.join(sys.path[0],"testset",str(int(IdList[i]))+".txt")
            file2 = os.path.join(sys.path[0],"testset",FpOutput+str(int(IdList[i]))+".txt")
            similarity = FileDiff().TwoFileSimilarity(file1,file2)
            FpPara.write("------------------start--------------------")
            FpPara.write("limit_len:\t"+str(limit_len)+"limit_ratio:\t"+
                             str(limit_ratio)+"limit_num\t"+str(limit_num)+"max_num\t"+str(max_num))
            FpPara.write("TwoFileSimilarity:\t"+str(similarity))
            if(similarity>opt_similarity):
                opt_limit_len = limit_len
                opt_limit_ratio = limit_ratio
                opt_limit_num = limit_num
                opt_max_num = max_num

def GetTrans(limit_len, limit_ratio, limit_num, max_num):
    ReUrlFile = "OutputUrl.csv"
    ErrorFile = "ErrorAdj.txt"
    FpOutput = 'trans'

    if os.path.exists(ReUrlFile):
        os.remove(ReUrlFile)#删除上一次重新爬取的链接
    else:
        pass
    FpError = open(ErrorFile, 'a')
    FpError.write("start:\t" + time.ctime() + "\n\n")
    TestFile = os.path.join(sys.path[0], "testset", "nju.csv")
    print TestFile
    Spider3(TestFile, FpError, FpOutput, limit_len, limit_ratio, limit_num, max_num)
    if os.path.exists(ReUrlFile):
        # 重新爬取Url，针对无法爬取的url
        FpError.write("-----Respider-----\n")
        print '-----respider-----\n'
        Spider3(ReUrlFile, FpError, FpOutput, limit_len, limit_ratio, limit_num, max_num)
    else:
        print 'No Connection aborted part'

    FpError.write("stop:\t"+time.ctime()+"\n\n")
    FpError.close()
