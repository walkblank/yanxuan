from dataclasses import dataclass, field
from typing import List


@dataclass 
class Item:
    itemId : str
    url : str
    category: str
    name: str
    realPrice: int
    originalPrice: int
    soldCount: int

    description : str = ''
    shopID: int = 0
    vendorID: str = ''
    commentCount: int = 0
    goodCommentCount: int = 0
    generalCommentCount: int = 0
    poorCommentCount: int = 0
    favorDesc1: str = ''
    favorDesc2: str = ''
    
@dataclass 
class SuperCategory:
    superCateId: str
    superCateName: str
    url: str
 

@dataclass
class Category(SuperCategory): 
    name: str
    # superCateName: str
    # url : str
    cateId: str
    # superCateId: str
    # itemList : List[Item] = field(default_factory=list)
    # topItem : Item

    # def addItem(self, item:Item):
        # self.itemList += item
        # self.itemList.append(item)
        # return self.itemList

    # def exportToFile(self):
        # pass

    # def update(self, dic: dict):
        # for key in dic.keys():
            # pass

  

@dataclass 
class EMall: 
    shopName: str
    superCateList : List[SuperCategory] = field(default_factory=list)
    cateList: List[Category]  = field(default_factory=list)
    
    def exportToFile(self):
        pass


if __name__ == "__main__":
    yxMall = EMall('yanxuan')
    # pass
