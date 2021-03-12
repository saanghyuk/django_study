#Section11
#파이썬 외부 파일 처리
#파이썬 Excel, CSV 파일 읽기 및 쓰기

#CSV : MIME - text/csv

import csv
#example1
with open('./resource/sample1.csv', 'r', encoding='utf-8') as f:
  reader = csv.reader(f)
  print("============print(reader)===============")
  print(reader)
  print("============next(reader)===============")
  next(reader) # skip header
  print("============print(dir(reader))===============")
  print(dir(reader))
  print("==========for=============")
  for c in reader:
    print(c)

#example2
with open('./resource/sample2.csv', 'r', encoding='utf-8') as f:
  reader = csv.reader(f, delimiter='|')
  print(reader)
  next(reader) # skip header
  print(dir(reader))
  for c in reader:
    print(c)

#example3, Dic Convert
print("=======example3=======")
with open('./resource/sample1.csv', 'r', encoding='utf-8') as f:
  reader = csv.DictReader(f)
  print(reader)
  for c in reader:
    for k, v in c.items():
      print(k, v)
    print()
    print('----------------')


#example 4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13 ,14, 15], [16, 17, 18]]

with open('./resource/sample3.csv', 'w', newline='') as f:
  wt = csv.writer(f)

  for v in w:
    print(v)
    wt.writerow(v)


#example5
with open('./resource/sample4.csv', 'w', newline='') as f:
  wt = csv.writer(f)
  wt.writerows(w)


#XSL, XLSX
#openpyxl, xlsxwriter, xlrd, wlwt, xlutils
#Mainly we use pandas
#pip install xlrd
#pip install openpyxl
#pip install pandas

import pandas as pd

#sheetname ='sheetname', header=int, skiprow=int
xlsx = pd.read_excel('./resource/sample.xlsx')
print(xlsx.head())
print()

print(xlsx.tail())
print(xlsx.shape)

#Excel or CSV
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.xlsx', index=False)
