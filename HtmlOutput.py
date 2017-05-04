# -*- coding:utf-8 -*-
import json
import sys
import pylab as pl
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

    def OutPlot(self, plot_pots):
    	limit_len = 4
    	limit_ratio = 0.1
    	limit_num = 8
    	cal_num = 0

    	x = []
    	y = []
    	record_ratio = []
    	num_pots = len(plot_pots)
    	# for pots in plot_pots:
    	# 	if pots[1] > limit_len:
    	# 		x.append(pots[0])
    	# 		y.append(pots[1])
    	for i in range(num_pots-1):
    		num1 = plot_pots[i+1][1] - plot_pots[i][1]#求解斜率，作为分子
    		num2 = plot_pots[i+1][0] - plot_pots[i][0]#作为分母
    		record_ratio.append(1.0*num1/num2)
    		print 1.0*num1/num2
    		print "\n"

    	for i in range(num_pots-1):
    		if(abs(record_ratio[i]) <= limit_ratio):
    			cal_num += 1
    		else:
    			if(cal_num > limit_num):
    				plot_pots[i-cal_num:i] = [0,0]
    				cal_num = 0
    			else:
    				cal_num = 0

    	for pots in plot_pots:
    		if isinstance(pots,list):
    			x.append(pots[0])
    			y.append(pots[1])
    	pl.plot(x, y, 'o')
    	pl.show()


