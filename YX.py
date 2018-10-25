import requests
import json, xlwt
from bs4 import BeautifulSoup
from dataclasses import dataclass
from eMall import EMall, Category, Item, SuperCategory
from typing import List


class YX(object):
    def __init__(self):
        print('yanxuan instant')

    def getEMall(self) -> EMall:
        yxMall = EMall('yanxuan')
        homePage = requests.get('http://you.163.com')
        if homePage.status_code:
            print(homePage.status_code)
        soup = BeautifulSoup(homePage.text, 'html.parser')
        content = soup.find_all('script')[7].text
        jsonData = content[content.find('{'): -1]
        jsonDict = json.loads(jsonData)
        for cate in jsonDict['cateList']:
            superCategory = SuperCategory(superCateName=cate['name'], superCateId=cate['id'],
                                          url='item/list?categoryId='+str(cate['id']))
            for subCate in cate['subCateList']:
                category = Category(name=subCate['name'], url='item/list?categoryId='+str(cate['id']),
                                    cateId=subCate['id'], superCateId=subCate['superCategoryId'],
                                    superCateName=cate['name'])
                yxMall.cateList += [category]
            yxMall.superCateList += [superCategory]
        return yxMall

    def getItemListOfCate(self, cate: Category) -> List[Item]:
        itemList = []
        url = 'http://you.163.com/' + cate.url
        print(url)
        print(cate.name)
        pageSrc = requests.get(url)
        soup = BeautifulSoup(pageSrc.text, 'html.parser')
        content = soup.find_all('script')[7].text
        jsonData = content[content.find('{'): -2]
        # print(jsonData)
        jsonDict = json.loads(jsonData)
        for cateT in jsonDict['categoryItemList']:
            if cateT['category']['name'] == cate.name:
                for item in cateT['itemList']:
                    # TODO
                    it = Item(name=item['name'], itemId=item['id'], category=cateT['category']['name'],
                              realPrice = item['retailPrice'], originalPrice = item['counterPrice'],
                              soldCount = item['sellVolume'], url= 'www')
                    # print(it)
                    itemList += [it]
                    # pass
                #
                break
            print('not found')
        return itemList

    def getItemListOfMall(self, export=True):
        if export:
            print('export')
        # pass


if __name__ == "__main__":
    yx = YX()
    yxMall = yx.getEMall()
    # print(yxMall)
    yx.getItemListOfCate(yxMall.cateList[0])
    yx.getItemListOfMall(False)
    yx.getItemListOfMall()
