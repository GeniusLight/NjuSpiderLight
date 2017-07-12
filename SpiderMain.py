# -*- coding:utf-8 -*-
import HtmlInput
import HtmlOutput
import HtmlDownloader
import HtmlDeal
import time
from FileCompare import FileDiff
import re
from goose import Goose
from goose.text import StopWordsChinese

ErrorFile = "error.txt"#请手动清除
OutputFile = "result.json"
UrlFile = "id_url_langua.csv"
ReUrlFile = 'OutputUrl.csv'

model_list = [
"test small set of url(0)",
"test model(1)"
]
for model_item in model_list:
    print model_item

#model_num = raw_input("Choose the model num:\n")
model_num = 0

if int(model_num) == 0:
    start_time = time.time()
    InputUrl = HtmlInput.InputUrl()
    Downloader = HtmlDownloader.Downloader()
    SimpleDeal = HtmlDeal.SimpleDeal()
    OutputContent = HtmlOutput.OutputContent()

    FpError = open(ErrorFile, 'a')
    FpError.write("start:\t" + time.ctime() + "\n\n")
    FpOutput = open(OutputFile, 'w')

    id_list = InputUrl.ReadId(UrlFile)
    url_list = InputUrl.ReadUrl(UrlFile)
    language_list = InputUrl.ReadLanguage(UrlFile)

    num = len(url_list)

    for i in range(num):
        html_text = Downloader.StaticDownload(url_list[i], int(id_list[i]), FpError)
        print ("id:%s\t\turl:%s")%(id_list[i], url_list[i])

        if language_list[i] == "chinese":
            g = Goose({"stopwords_calss":StopWordsChinese})
            try:
                article = g.extract(url=url_list[i])
                content = article.cleaned_text
                title = article.title
            except Exception as e:
                FpError.write("can't extract it\n id:%s\t\tcontent:%s\n")(id_list[i]. url_list[i])
                FpError.write("ratio is:%f")%(ratio)
                content = ""
                title = ""

        elif language_list[i] == "english":
            g = Goose()
            try:
                article = g.extract(url=url_list[i])
                content = article.cleaned_text
                title = article.title
            except Exception as e:
                FpError.write("can't extract it\n id:%s\t\tcontent:%s\n")(id_list[i]. url_list[i])
                FpError.write("ratio is:%f")%(ratio)
                content = ""
                title = ""


        elif language_list[i] == "unknow":
            g = Goose()
            try:
                article = g.extract(url=url_list[i])
                content = article.cleaned_text
                title = article.title
            except Exception as e:
                FpError.write("can't extract it\n id:%s\t\tcontent:%s\n")(id_list[i]. url_list[i])
                FpError.write("ratio is:%f")%(ratio)
                content = ""
                title = ""
                print content

        elif language_list[i] == "nocontent":
            content = ""
            title = ""


        output_es = HtmlDeal.SimpleTrs(title, content, url_list[i])
        OutputContent.OutputEs(output_es, int(id_list[i]), FpOutput)
    
    stop_time = time.time()
    print ("use time:%f")%(stop_time-start_time)


    start_time = time.time()
    start_time = time.time()


if int(model_num) == 1:
    url = "https://xgc.nju.edu.cn/5e/81/c1521a24193/page.htm"
    g = Goose({"stopwords_class":StopWordsChinese})
    #g = Goose()
    article = g.extract(url=url)
    print article.title
    print article.cleaned_text
