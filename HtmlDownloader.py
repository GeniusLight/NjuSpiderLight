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
            fp_error.write(url+'\t'+str(e)+'\t'+"\n")
            return None

        html_text = html.text
        return html_text


