# -*- coding:utf-8 -*-
import requests


class Downloader(object):
    def StaticDownload(self, url, fp_error): #Get the static content of the web page
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"}
        if url is None:
            return None

        try:
            html = requests.get(url, headers=headers)
        except Exception as e:
            fp_error.write("location1"+"\t"+url+'\t\t'+str(e)+'\t'+"\n")
            return None
        if html.encoding == 'ISO-8859-1': #中英文网页的编码问题
            html_text = html.text
            html_text = html_text.decode("utf8").encode("ISO-8859-1")
        else:
            html_text = html.text

        return html_text


