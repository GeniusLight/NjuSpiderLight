#coding:utf-8
import jieba
from difflib import unified_diff

class FileDiff(object):
    def TwoFileCompare(self, file1, file2):
        fp1 = open(file1, "r")
        fp2 = open(file2, "r")
        content1 = ""
        content2 = ""
        for i in fp1.readlines():
            content1 = content1 + i
        for i in fp2.readlines():
            content2 = content2 + i
        list1 = jieba.cut(content1, cut_all=False)
        list2 = jieba.cut(content2, cut_all=False)
        for line in unified_diff(list1, list2, fromfile="before.py", tofile ="after.py"):
            sys.stdout.write(line)
