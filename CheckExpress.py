# -*- coding:utf-8 -*-
__auther__ = 'slll.info'
__date__ = '2016-7'
#module import
import requests,json
#function
def spider(type,id):
	url = 'https://www.kuaidi100.com/query?type=%s&postid=%s' %(type,id)
	data = requests.get(url)
	json = data.json()
	if json['status'] == "200":
		data_json = json['data']
		print("//////////////快递详细信息//////////////")
		for x in data_json:
			print("%s : %s" %(x['time'],x['context']))
	else:
		print("错误的快递单号!")

def express_type_get():
	express_type = ('shunfeng','yunda','shentong','yuantong','zhongtong','ems','tiantian','huitongkuaidi','quanfengkuaidi','youzhengguonei')
	print('////////////////快递公司////////////////\n1.顺丰	2.韵达	3.申通	4.圆通	5.中通\n6.EMS	7.天天	8.汇通	9.全峰	10.邮政\n////////////////////////////////////////')
	while True:
		express = int(input('请选择快递公司(数字):'))
		if express:
			if express <= 10 and express >= 1:
				break
			else:
				print("错误的选择!")
		else:
			print("不能为空!")
	return express_type[express-1]
def express_id_get():
	while True:
		express_id = input('请输入快递单号:')
		if express_id:
			break
		else:
			print("快递单号不能为空!")
	return express_id
#Mainprogram
kd = express_type_get()
kd_id = express_id_get()
spider(kd,kd_id)