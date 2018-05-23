#coding=utf-8
import requests
from bs4 import BeautifulSoup
import json


class YanXuanItem:
	def __init__(self):
		self.name = ''
		self.id = ''
		self.resultItems = []


class YanXuan:

	def __init__(self):
		self.baseUrl = 'http://you.163.com/item/list?'
		self.payload = {}
		self.title = ''
		# self.search_url = 'http://you.163.com/item/list?'
		self.soup = BeautifulSoup('', 'html.parser')
		self.pyData = {}
		self.result = {}
		self.superCategory = {'居家': '1005000', '配件': '1008000', '服装': '1010000', '电器': '1043000',
		                      '洗护': '1013001','饮食': '1005002', '餐厨': '1005001', '婴童': '1011000',
							 '文体': '1019000', '特色区': '1065000'}

		self.searchCategoryList = {}
		self.searchItemList = {}

	def set_payload(self, params):
		self.payload.update(params)

	def clear_payload(self):
		self.payload.clear()

	def get_category_pydata(self):
		searchUrl = self.baseUrl
		for key in self.payload:
			searchUrl += (key + '='+self.payload[key]+'&')
		print(searchUrl)
		searchPage = requests.get(searchUrl)
		searchSoup = BeautifulSoup(searchPage.text, 'html.parser')
		# print(search_soup)
		jsonData = searchSoup.find_all('script')[7].text[15:-2]
		# print(jsonData)
		# print('len = ', len(jsonData))
		# [7].text[15:-2]
		self.pyData = json.loads(jsonData)
		# print(self.py_data)

	def get_all_category_list(self):
		# main_url = 'http://you.163.com'
		# main_page = requests.get(main_url)
		# file = open('itemlist.txt', 'w+')
		for val in self.superCategory.values():
			searchUrl = self.baseUrl + 'categoryId=' + val +'&timer=tc'
			print(searchUrl)
			searchPage = requests.get(searchUrl)
			searchSoup = BeautifulSoup(searchPage.text, 'html.parser')
			jsonData = searchSoup.find_all('script')[7].text[15:-2]
			pyData = json.loads(jsonData)

			for cate in pyData['categoryItemList']:
				print('*==='+cate['category']['name']+'===*')
				# file.writelines(cate['category']['name'] + '\n')
			# self.searchCategoryList.append((str(cate['category']['name']), cate['category']['id']))
			# self.searchCategoryList.append({cate['category']['name']: cate['category']['id'], "itemIDList": []})
				self.searchCategoryList[cate['category']['id']] = []
				for item in cate['itemList']:
					# print(item['name'], item['id'])
					# price = str(item['counterPrice'])
					# print(type(price))
					# print(type(item['name']))
					# sellVolume = str(item['sellVolume'])
					# file.writelines(item['name']+'#'+str(item['id'])+'#'+str(item['rank'])+'#'+price+'#' + sellVolume + '\n')
					print(item['name'], '#', item['id'], '#', item['rank'], '#', item['sellVolume'], '#', item['counterPrice'])
					self.searchCategoryList[cate['category']['id']].append(item['id'])
			# print(cate['category']['name'])
		print(self.searchCategoryList)
		# file.close()



	def get_search_category_list(self):
		print(self.pyData.keys())
		# print(self.py_data['categoryItemList'], len(self.py_data['categoryItemList']))
		print(self.pyData['categoryItemList'][1].keys())
		for cate in self.pyData['categoryItemList']:
			print('*==='+cate['category']['name']+'===*')
			# self.searchCategoryList.append((str(cate['category']['name']), cate['category']['id']))
			# self.searchCategoryList.append({cate['category']['name']: cate['category']['id'], "itemIDList": []})
			self.searchCategoryList[cate['category']['id']] = []
			for item in cate['itemList']:
				print(item['name'], item['id'])
				self.searchCategoryList[cate['category']['id']].append(item['id'])
			# print(cate['category']['name'])
		print(self.searchCategoryList)
		print(self.pyData['categoryItemList'][1]['category'])
		# print(self.py_data['categoryItemList'][1]['itemList'])
		# print(self.pyData['categoryItemList'][0]['itemList'][3])
		# pass

	def export_result(self):
		pass


if __name__ == '__main__':
	yx = YanXuan()
	# yx.set_payload({'categoryId': '1005001', 'subCategoryId': '1005007', "timer": 'tc'})
	# yx.get_category_pydata()
	# yx.get_search_category_list()
	yx.get_all_category_list()

