import openpyxl
wb = openpyxl.Workbook()
sheet = wb['Sheet']
sheet['A1'] = 'Hello world!'
print(sheet['A1'].value)
print(wb.get_sheet_names())
wb.save('temp1.xlsx') # 保存的时候，如果之前的这个excel文件打开会报错，关闭重新运行就可以了。
'Hello world!'