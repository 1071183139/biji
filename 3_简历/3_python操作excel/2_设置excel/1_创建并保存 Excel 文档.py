import openpyxl
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
sheet = wb.active

# # change the name of the sheet
print(sheet.title)
sheet.title = 'Happy2017'
print(sheet.title)
wb.save