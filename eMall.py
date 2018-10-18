from dataclasses import dataclass, field
from typing import List


@dataclass 
class Item:
    itemID : str
    url : str
    category: str
    name: str
    realPrice: int
    orignalPrice: int
    description : str
    shopID: int
    vendorID: str
    soldCount: int
    commentCount: int
    goodCommentCount: int
    generalCommentCount: int
    poorCommentCount: int
    favorDesc1: str
    favorDesc2: str

@dataclass
class Category: 
    name: str
    url : str
    cateID: str
    itemList : List[Item] # = field(default_factory=list)
    topItem : Item

    def addItem(self, item:Item) -> List[Item]:
        self.itemList.append(item)
        # return self.itemList
    
@dataclass 
class EMall: 
    shopName: str
    cateList: List[Category] # = field(default_factory=list)