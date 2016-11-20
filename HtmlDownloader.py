import requests
import dryscrape


class Downloader(object):
    def StaticDownload(self, url): #Get the static content of the web page
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"}
        if url is None:
            return None
        html = requests.get(url, headers=headers)
        html_text = html.text

