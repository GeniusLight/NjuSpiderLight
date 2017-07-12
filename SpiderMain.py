# -*- coding:utf-8 -*-
import HtmlInput
import HtmlOutput
import HtmlDownloader
import HtmlDeal
import time
import os
import csv
import sys
import json
import urllib2
from FileCompare import FileDiff

ErrorFile = "error.txt"#请手动清除
OutputFile = "result.json"
UrlFile = "id_url_new.csv"
ReUrlFile = 'OutputUrl.csv'

