# we use xlwings to read/write excel files and sort the data with other library

# import xlwings as xw

import xlrd
import xlwt
import sqlite3

PRIMARY_CATEGORY = 'kitchenware'

# wb = xw.Book("category.xlsx")
# sheet = wb.sheets[0]
# # sheet = wb.sheets.active
# print(sheet.range('A1').expand('right').value)
# print(sheet.range('A2').expand('right').value)
#
# print(set(sheet.range('B2').expand('down').value))
# print(set(sheet.range('C1').expand('down').value))

excel_book = xlrd.open_workbook("category.xlsx")
print(excel_book.sheet_names())
sheet1 = excel_book.sheet_by_index(0)
print(sheet1.name, sheet1.nrows, sheet1.ncols)
date = sheet1.col_values(0)[1:]
print(set(date))
date_1 = xlrd.xldate_as_datetime(date[1], excel_book.datemode)
print(date_1)
sales_by_time = {}
rows = sheet1.row_values(1)
cols0 = sheet1.col_values(2)[1:]
cols = sheet1.col_values(3)[1:]


print(rows)
print(len(cols0), len(set(cols0)), set(cols0))
print(len(cols),len(set(cols)) ,set(cols))


conn = sqlite3.connect("test.db")
c = conn.cursor()
print("connect database successfully")

# cursor = c.execute()

