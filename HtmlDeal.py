# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import json


class SimpleTrs(object):
    def __init__(self, title, content, url):
        self.title = title
        self.content = content
        self.url = url

class SimpleDeal(object):
    def Method1(self, url, html_text, fp_error):
        if html_text is None:
            OutputS = SimpleTrs(None, None, url)
            return OutputS

        html_text = html_text.replace('&nbsp;', '') #处理源码中不需要的字符
        html_text = html_text.replace('\s*', ',')
        html_text = html_text.replace('&emsp;', ',')

        soup = BeautifulSoup(html_text, "lxml")
        script = soup.find_all("script")  # 找到所有script的标签
        for x in script:  # 判断script标签是否包含文本，若有，直接置为空
            if x.string != None:
                x.string.replace_with(" ")

        style = soup.find_all("style")  # 找到所有script的标签
        for x in style:  # 判断script标签是否包含文本，若有，直接置为空
            if x.string != None:
                x.string.replace_with(" ")

        try:
            title = soup.title.string.strip()
        except Exception as e:
            fp_error.write("location2"+"\t"+url + '\t' + str(e) + '\t' + "\n")  # 出现读出title为空的情况，不太明白
            title = "None"

        content = "\t".join(soup.stripped_strings)
        OutputS = SimpleTrs(title, content, url)
        return OutputS

    def Method2(self, url, html_text, fp_error):
        pass