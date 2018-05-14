#coding=utf-8
import requests
from bs4 import BeautifulSoup
import json


class YanXuanItem():
	def __init__(self):
		self.name = ''
		self.id = ''
		self.resultItems = []


class YanXuan:

	def __init__(self):
		self.base_url = 'http://you.163.com/item/list?'
		self.payload = {}
		self.title = ''
		# self.search_url = 'http://you.163.com/item/list?'
		self.soup = BeautifulSoup('', 'html.parser')
		self.py_data = {}
		self.result =  {}

	def set_payload(self, params):
		self.payload.update(params)

	def get_pydata(self):
		search_url = self.base_url
		for key in self.payload:
			search_url += (key + '='+self.payload[key]+'&')
		print(search_url)
		search_page = requests.get(search_url)
		search_soup = BeautifulSoup(search_page.text, 'html.parser')
		# print(search_soup)
		json_data = search_soup.find_all('script')[7].text[15:-2]
		self.py_data = json.loads(json_data)
		# print(self.py_data)

	def get_all_category_list(self):
		main_url = 'http://you.163.com'
		main_page = requests.get(main_url)

		pass

	def get_search_category_list(self):
		print(self.py_data.keys())
		# print(self.py_data['categoryItemList'], len(self.py_data['categoryItemList']))
		print(self.py_data['categoryItemList'][1].keys())
		print(self.py_data['categoryItemList'][1]['category'])
		# print(self.py_data['categoryItemList'][1]['itemList'])
		print(self.py_data['categoryItemList'][1]['itemList'][1])
		pass

	def export_resualt(self):
		pass

if __name__ == '__main__':
	yanxuan = YanXuan()
	yanxuan.set_payload({'categoryId':'1005001', 'subCategoryId':'1005007'})
	yanxuan.get_pydata()
	yanxuan.get_search_category_list()
#
# payload = {'categoryId':'1005001', 'subCategoryId':'1005007'}
# yanxuan_page = requests.get('http://you.163.com/item/list', params = payload)
# # print(yanxuan_page.text)
# yanxuan_soup = BeautifulSoup(yanxuan_page.text, 'html.parser')
# # print(yanxuan_soup)
# f = open('yanxuan.html', 'w+')
# f.write(str(yanxuan_soup))
# print('-start to search-')
# script_list = yanxuan_soup.find_all('script')
# target_list = script_list[7]
# print(type(target_list))
# json_data = target_list.text[15:-2]
# print(target_list.text[15:-2])
# print(type(target_list.text))
# # sep = target_list.text.split('=')
# # print(len(sep))
# # print(sep[2]) # print(sep[3])
# # json_data = sep[1] +'='+sep[2]+ '=' + sep[3]
# # f = open('json.txt', 'w+')
# # f.write(json_data)
# f.close()
#
# python_data = json.loads(json_data)
# print(python_data.keys())
# # ['deliveryAreaList', 'currentCategory', 'indexBannerItemVO', 'focusList', 'categoryItemList', 'pathList']
# # print(type(python_data['categoryItemList']))
# # print(len(python_data['categoryItemList']))
# # print(python_data['categoryItemList'][3])
# # print(type(python_data['categoryItemList'][3]))
# # categoryItemList   len = 7
# categoryItemList = python_data['categoryItemList']
# # for category in  categoryItemList:
# # 	print(category['category'])
# # 	if category['category']['name'] == '锅具':
# # 		# print(category['itemList'])
# # 		for item in category['itemList']:
# # 			print(item['name'], item['seoTitle'])
#
#
# earned_money = 0
# single_best_amount = 0
# best_sold_item = {}
# for category in  categoryItemList:
# 	print(category['category']['name'])
# 	# print(category['itemList'])
# 	for item in category['itemList']:
# 		# print(item)
# 		print('id:', item['id'], '#', item['rank'], '#', item['name'], '#',item['seoTitle'], '#', item['counterPrice'], '#', item['sellVolume'])
# 		single_amount = item['counterPrice'] * item['sellVolume']
# 		if single_amount > single_best_amount:
# 			single_best_amount = single_amount
# 			# best_sold_item.clear()
# 			best_sold_item = item
# 		earned_money = earned_money + item['counterPrice']*item['sellVolume']
#
# print('best sold:', single_best_amount, best_sold_item['id'], '排名:', best_sold_item['rank'], best_sold_item['name'], best_sold_item['seoTitle'], '价格：', best_sold_item['counterPrice'], '卖出:', best_sold_item['sellVolume'])
# print("earned = :", earned_money)
# print(categoryItemList[0].keys())
# # ['filterParams', 'itemList', 'category']
# print(categoryItemList[0]['category'])
# print(type(categoryItemList[0]['itemList']))
# print(len(categoryItemList[0]['itemList']))
# itemList = categoryItemList[0]['itemList']
# item = itemList[0]
# print(type(item))
# print(item.keys())