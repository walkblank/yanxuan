import requests
from bs4 import BeautifulSoup
import json
from dataclasses import dataclass
import xlwt
from eMall import EMall, Category, Item


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
        cate = Category()
        for cate in jsonDict['cateList']:
            yxMall.cateList 

        return yxMall
        

    def getItemListOfCate(self, cate: Category):
        pass
        

if __name__  == "__main__":
    yx = YX()
    yx.getEMall()
