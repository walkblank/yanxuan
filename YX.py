import requests, json, xlwt
from bs4 import BeautifulSoup
from dataclasses import dataclass
from eMall import EMall, Category, Item, SuperCategory
from typing import List
from retrying import retry #pip install retrying

@retry(stop_max_attempt_number = 5)
def getPageContent(url:str) -> dict:
    pageSrc = requests.get(url)
    # print(pageSrc.status_code)
    soup = BeautifulSoup(pageSrc.text, 'html.parser')
    content = soup.find_all('script')[7].text
    #extract the real json struct data 
    #find and rfind
    jsonData = content[content.find('{') : content.rfind('}')+1]
    return json.loads(jsonData)


class YX(object):
    def __init__(self):
        print('yanxuan instant')

    def getEMall(self) -> EMall:
        yxMall = EMall('yanxuan')
        
        jsonDict = getPageContent('http://you.163.com') 
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

    def getItemListOfCate(self, cateList: List[Category]) -> List[Item]:
        itemList = []
        urlSet = set()
        cateNameSet = set()
        for cate in cateList:
            urlSet.add(cate.url)
            cateNameSet.add(cate.name)
        print(urlSet)
        for i in urlSet:
            url =  'http://you.163.com/'+ i + '&timer=tc' 
            print(url)
            jsonDict = getPageContent(url)
            for cateT in jsonDict['categoryItemList']:
                if cateT['category']['name'] in cateNameSet:
                    for item in cateT['itemList']:
                        it = Item(name=item['name'], itemId=item['id'], category=cateT['category']['name'],
                                  realPrice=item['retailPrice'], originalPrice=item['counterPrice'],
                                  soldCount=item['sellVolume'], url='www')
                        # print(it)
                        itemList += [it]
        return itemList

    def getItemListOfSuperCate(self, superCateList: List[SuperCategory]):
        itemList = []
        cateList = []
        for superCate in superCateList:
            jsonDict = getPageContent('http://you.163.com/'+superCate.url+'&timer=tc')
            for cateT in jsonDict['categoryItemList']:
                # print(cateT['category'])
                # print(superCate.superCateName)
                category = Category(name=cateT['category']['name'],superCateName=superCate.superCateName,
                                    cateId=cateT['category']['id'], superCateId=cateT['category']['superCategoryId'],
                                    url='item/list?categoryId='+ str(superCate.superCateId))
                cateList += [category]
                for item in cateT['itemList']:
                    it = Item(name=item['name'], itemId=item['id'], category=cateT['category']['name'],
                                  realPrice=item['retailPrice'], originalPrice=item['counterPrice'],
                                  soldCount=item['sellVolume'], url='www')
                    # print(it)
                    itemList += [it]
                
        return itemList, cateList

    def getItemInfo(self, item: Item):
        pass


    def getItemListOfMall(self, export=True):
        if export:
            print('export')
        # pass

def userInterfaceShell():
    itemList = []
    searchCateList = []
    yx= YX()
    yxmall = yx.getEMall()
    for i in yxmall.superCateList:
        print(yxmall.superCateList.index(i), i.superCateName)
    print('______________')
    print('你想搜索哪个品类?')
    cateSelect = input('请输入==>')
    selectSuperCate = yxmall.superCateList[int(cateSelect)]
    print('你选择了:', selectSuperCate.superCateName)
    print('______________')
    print('请继续选择：')
    print('1 搜索整个品类')
    print('2 搜索子品类')
    print('______________')
    select = input('请输入==>')

    (itemList, searchCateList) = yx.getItemListOfSuperCate([selectSuperCate])
    if select == '1':
        #TODO export itemList to excel file
        # print(itemList)
        pass
    if select == '2':
        print('______________')
        print('子品类列表:')
        for cate in  searchCateList:
            print(searchCateList.index(cate), cate.name)
        print('______________')
        print('请选择想要搜索的子品类:')
        cateItemSelect = input("请输入==>")
        print(cateItemSelect)
        l = cateItemSelect.split(' ')
        searchList = []
        for i in l:
            searchList += [searchCateList[int(i)]]
        print(searchList)
        itemList = yx.getItemListOfCate(searchList)


if __name__ == "__main__":
    # itemList = []
    # searchCateList = []
    # book = xlwt.Workbook()
    # sheet = book.add_sheet('sport')
    # writeRow = 0
    # yx = YX()
    # yxMall = yx.getEMall()
    # print(yxMall)
    # print(yxMall.superCateList)
    # print(yxMall.cateList)
    # for i in yxMall.cateList:
    #     if i.superCateName == '服装':
    #         print(yxMall.cateList.index(i),i)
    # for i in range(38,44):
    #     searchCateList += [yxMall.cateList[i]]
    # itemList = yx.getItemListOfCate(cateList = searchCateList)
    # print(itemList)
    # print(yxMall.superCateList[0])
    # yx.getItemListOfSuperCate([yxMall.superCateList[0]])
    # for i in yxMall.superCateList:
    #     print(yxMall.superCateList.index(i),  i.superCateName)

    userInterfaceShell()
    while True:
        print('______________')
        print('搜索完成，是否继续搜索:')
        print("0 继续")
        print("1 退出")
        print('______________')
        select = input("请输入==>")
        if select == '0':
            userInterfaceShell()
        if select == '1':
            break
