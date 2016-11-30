# -*- coding:utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class OutputContent(object):
    def OutputEs(self, content, id, FpOutput):
        json_data = {"create": {"_index": "njusearch3", "_type": "test1", "_id": id}}
        json_data = json.dumps(json_data)
        FpOutput.write(json_data)
        FpOutput.write("\n")
        FpOutput.write(json.dumps(content, default=lambda obj: obj.__dict__, ensure_ascii=False))  # 序列化输出
        FpOutput.write("\n")
