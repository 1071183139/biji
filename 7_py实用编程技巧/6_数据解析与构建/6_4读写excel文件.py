# import xlrd, xlwt
#
# rbook = xlrd.open_workbook('demo.xlsx')  # 打开excel文件
#
# # 获取所有的 表  rbook.sheets()     一个excel文件 是有多个表构成的 即sheet  可以在文件底边看到当前是哪张表
# rsheet = rbook.sheet_by_index(0)  # 第一张表
#
# k = rsheet.ncols  # ncols 列     nrows 行
# rsheet.put_cell(0, k, xlrd.XL_CELL_TEXT, '总分', None)  # 放置一个单元格，内容格式是文本，内容是总分
#
# for i in range(1, rsheet.nrows):
#     t = sum(rsheet.row_values(i, 1))  # 算总分
#     rsheet.put_cell(i, k, xlrd.XL_CELL_NUMBER, t, None)
#
# wbook = xlwt.Workbook()
# wsheet = wbook.add_sheet(rsheet.name)  # 表名不变
#
# # 将原来的分数  和新添加的  总分 保存在新的excel文件中
# for i in range(rsheet.nrows):
#     for j in range(rsheet.ncols):
#         wsheet.write(i, j, rsheet.cell_value(i, j))
#
# wbook.save('out.xlsx')





















