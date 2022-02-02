
# import xlrd
# import pandas as pd
# import numpy as np

# file = "C:\\Users\\admin\\Downloads\\product-screener.xls"
# file = "C:\\Users\\admin\\Downloads\\product-screener.xlsx"

# x = np.genfromtxt(file, dtype=None, encoding='utf-8-sig')
# x = np.genfromtxt(file, dtype=None, encoding=None)
# book  = xlrd.open_workbook(file)

# df = pd.DataFrame(x)

# df = pd.read_excel(file, engine='openpyxl')
# df = pd.read_excel(file, sheet_name='All funds', engine='xlrd', skiprows=2)
# df = pd.read_table(file)
# df = df['<?xml version="1.0"?>'].str.split("</Row>", expand=True)
# df = pd.read_xml(file, xpath=".//cell")


# print('got here')

# print(df)

# method 1 - read excel
# file = "C:\\Users\\admin\\Downloads\\product-screener.xls"
# df = pd.read_excel(file)
# print(df)


# method 2 - pip install xlrd and use engine
# file = "C:\\Users\\admin\\Downloads\\product-screener.xls"
# df = pd.read_excel(file, engine='xlrd')
# print(df)



# method 3 - rename to xlsx and open with openpyxl
# file = "C:\\Users\\admin\\Downloads\\product-screener.xlsx"
# df = pd.read_excel(file, engine='openpyxl')
# print(df)


# method 4 - use read_xml
# file = "C:\\Users\\admin\\Downloads\\product-screener.xls"
# df = pd.read_xml(file)
# print(df)



# method 5 - use read_table
# file = "C:\\Users\\admin\\Downloads\\product-screener.xls"
# df = pd.read_table(file)
# print(df)


# method 5 - use read_html
# file = "C:\\Users\\admin\\Downloads\\product-screener.xls"
# df = pd.read_html(file)
# print(df)


# method 6 - convert xml programatically with class
# import pandas as pd
# from xml.sax import ContentHandler, parse

# file = "C:\\Users\\admin\\Downloads\\product-screener.xls"

# # Reference https://goo.gl/KaOBG3
# class ExcelHandler(ContentHandler):
#     def __init__(self):
#         self.chars = [  ]
#         self.cells = [  ]
#         self.rows = [  ]
#         self.tables = [  ]
#     def characters(self, content):
#         self.chars.append(content)
#     def startElement(self, name, atts):
#         if name=="Cell":
#             self.chars = [  ]
#         elif name=="Row":
#             self.cells=[  ]
#         elif name=="Table":
#             self.rows = [  ]
#     def endElement(self, name):
#         if name=="Cell":
#             self.cells.append(''.join(self.chars))
#         elif name=="Row":
#             self.rows.append(self.cells)
#         elif name=="Table":
#             self.tables.append(self.rows)

# excelHandler = ExcelHandler()
# parse(file, excelHandler)
# df = pd.DataFrame(excelHandler.tables[0][4:], columns=excelHandler.tables[0][3])

# print(df)


# method 7 - convert xml programatically with xml.etree
import pandas as pd
import xml.etree.ElementTree as ET

import shutil

file_xls = "C:\\Users\\admin\\Downloads\\product-screener.xls"
file_xml = 'C:\\Users\\admin\\Downloads\\product-screener.xml'

shutil.copyfile(file_xls, file_xml)

tree = ET.parse(file_xml)
root = tree.getroot()

data = [[c[0].text for c in r] for r in root[1][0][2:]]
types = [c[0].get('{urn:schemas-microsoft-com:office:spreadsheet}Type') for c in root[1][0][2]]

df = pd.DataFrame(data)
df = df.replace('-', None)
for c in df.columns:
    if types[c] == 'Number':
        df[c] = pd.to_numeric(df[c])
    elif types[c] == 'DateTime':
        df[c] = pd.to_datetime(df[c])

print(df)

