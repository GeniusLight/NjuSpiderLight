#coding:utf-8
import HtmlOutput
from numpy import arange
import HtmlDownloader
import HtmlDeal
import HtmlOutput
import HtmlInput
import HtmlInput
import time
import datetime
import os
import sys
from FileCompare import FileDiff



limit_len = [6]
limit_ratio = arange(0,1.0,0.5)
limit_num = range(0,10,5)
max_num = range(0,20,10)
global opt_limit_len
opt_limit_len = 0
global opt_limit_ratio
opt_limit_ratio = 0
global opt_limit_num
opt_limit_num = 0
global opt_max_num
opt_max_num = 0
global opt_similarity
opt_similarity = 0



def Spider3(SpiderFile, FpError, FpOutput, limit_len, limit_ratio, limit_num, max_num):
    global opt_limit_len
    global opt_limit_ratio
    global opt_limit_ratio
    global opt_max_num
    global opt_similarity
    Downloader = HtmlDownloader.Downloader()
    SimpleDeal = HtmlDeal.SimpleDeal()
    OutputContent = HtmlOutput.OutputContent(limit_len, limit_ratio, limit_num, max_num)
    InputUrl = HtmlInput.InputUrl()
    IdList = InputUrl.ReadId(SpiderFile)
    UrlList = InputUrl.ReadUrl(SpiderFile)
    num = len(UrlList)
    similarity_all = 0

    FpPara.write("------------------start--------------------\n")
    FpPara.write("limit_len:"+str(limit_len)+"\t\tlimit_ratio:"+
                 str(limit_ratio)+"\t\tlimit_num:"+str(limit_num)+"\t\tmax_num:"+str(max_num)+"\n")
    for i in range(num):
        #print ("id:%d \t\t url:%s") % (int(IdList[i]), UrlList[i])
        html_path = os.path.join(sys.path[0],"testset",str(int(IdList[i]))+".html")
        html_text = Downloader.StaticRead(html_path)
        if html_text == None:
            pass
        else:
            out_pots = SimpleDeal.Method3(UrlList[i], html_text, FpError)
            OutputContent.TestSet(out_pots, int(IdList[i]), FpOutput)
            file1 = os.path.join(sys.path[0],"testset",str(int(IdList[i]))+".txt")
            file2 = os.path.join(sys.path[0],"testset",FpOutput+str(int(IdList[i]))+".txt")
            similarity = FileDiff().TwoFileSimilarity(file1,file2)
            FpPara.write("of file:"+str(int(IdList[i]))+"\tTwoFileSimilarity:\t"+str(similarity)+"\n")
            similarity_all = similarity_all+ similarity

    FpPara.write("The similarity add is:"+str(similarity_all)+"\n")

    if(similarity_all>opt_similarity):
        opt_similarity = similarity_all
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
    #print TestFile
    Spider3(TestFile, FpError, FpOutput, limit_len, limit_ratio, limit_num, max_num)
    FpError.write("stop:\t"+time.ctime()+"\n\n")
    FpError.close()

start_time = datetime.datetime.now()
print "start at:"+ str(start_time)

ParaRecord = "para.txt"
FpPara = open(ParaRecord,'w')
for i in limit_len:
    for j in limit_ratio:
        for k in limit_num:
            for l in max_num:
                GetTrans(i,j,k,l)

print "Have finished:\n"
print "opt_similarity:\t"+str(opt_similarity)
print "limit_len:\t"+str(opt_limit_len)
print "limit_ratio\t"+str(opt_limit_ratio)
print "limit_num\t"+str(opt_limit_num)
print "max_num\t"+str(opt_max_num)
FpPara.close()

end_time = datetime.datetime.now()
print "\nend at:"+str(end_time)
print "----------------------------------"
print "cost time:"+str((end_time-start_time).seconds)+"s"
