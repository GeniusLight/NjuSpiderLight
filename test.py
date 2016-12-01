# -*- coding:utf-8 -*-
import HtmlInput
import HtmlOutput
import HtmlDownloader
import HtmlDeal

url = 'http://stuex.nju.edu.cn/'
id = 1
ErrorFile = "error.txt"
FpError = open(ErrorFile, 'a')


Downloader = HtmlDownloader.Downloader()
SimpleDeal = HtmlDeal.SimpleDeal()
OutputContent = HtmlOutput.OutputContent()

html_text = Downloader.StaticDownload(url, FpError)
html_text = html_text.decode("utf8").encode("ISO-8859-1")
print html_text
# OutputS = SimpleDeal.Method1(url, html_text, None)
# OutputContent.OutputEs(OutputS, id, None)
