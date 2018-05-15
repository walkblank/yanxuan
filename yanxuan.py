#coding=utf-8
import requests
from bs4 import BeautifulSoup
import json

YANXUAN_CATLIST = [
		{''},
		{''},
		{''},
]


class YanXuanItem():
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
		self.superCategory = []
		self.search_CategoryList = []
		self.search_ItemList = []

	def set_payload(self, params):
		self.payload.update(params)

	def get_pydata(self):
		searchUrl = self.baseUrl
		for key in self.payload:
			searchUrl += (key + '='+self.payload[key]+'&')
		print(searchUrl)
		searchPage = requests.get(searchUrl)
		searchSoup = BeautifulSoup(searchPage.text, 'html.parser')
		# print(search_soup)
		jsonData = searchSoup.find_all('script')[7].text[15:-2]
		print(jsonData)
		print('len = ', len(jsonData))
		# [7].text[15:-2]
		self.pyData = json.loads(jsonData)
		# print(self.py_data)

	def get_all_category_list(self):
		main_url = 'http://you.163.com'
		main_page = requests.get(main_url)

		pass

	def get_search_category_list(self):
		print(self.pyData.keys())
		# print(self.py_data['categoryItemList'], len(self.py_data['categoryItemList']))
		print(self.pyData['categoryItemList'][1].keys())
		for cate in self.pyData['categoryItemList'] :
			print('*==='+cate['category']['name']+'===*')
			self.search_CategoryList.append((str(cate['category']['name']), cate['category']['id']))
			for item in cate['itemList']:
				print(item['name'], item['id'])
			# print(cate['category']['name'])
		print(self.search_CategoryList)
		print(self.pyData['categoryItemList'][1]['category'])
		# print(self.py_data['categoryItemList'][1]['itemList'])
		print(self.pyData['categoryItemList'][0]['itemList'][3])
		pass


	def export_resualt(self):
		pass


if __name__ == '__main__':
	yanxuan = YanXuan()
	yanxuan.set_payload({'categoryId':'1005001', 'subCategoryId':'1005007', "timer":'tc'})
	yanxuan.get_pydata()
	yanxuan.get_search_category_list()
