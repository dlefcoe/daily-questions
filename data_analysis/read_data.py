
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

