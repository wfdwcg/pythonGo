import xlrd
# 打开文件
# workbook = xlrd.open_workbook('testQuery.xlsx')
# sheet2_name = workbook.sheet_names() # 获取所有sheet名称
# print(sheet2_name)
# 根据sheet索引或者名称获取sheet内容
# sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
# sheet1 = workbook.sheet_by_name('sheet2')
# sheet1的名称，行数，列数
# print(sheet1.name, sheet1.nrows, sheet1.ncols)
# 获取整行和整列的值（数组）
# rows = sheet1.row_values(2) # 获取第三行内容
# cols = sheet1.col_values(0) # 获取第1列内容
# print(rows)
# print(cols)
# 获取单元格内容
# print(int(sheet1.cell(2, 0).value))
# print(sheet1.cell_value(2, 0))
# print(sheet1.row(2)[0].value)
# # 获取单元格内容的数据类型
# print(sheet1.cell(2, 0).ctype)

import sys
def printOut(ss):
    result = 'curl -d "key=173:'
    result += str(sys.argv[2])
    result += '&fieldAndValue='
    result += ss
    result += '" "http://127.0.0.1:8080/cccTest" '
    result += "--header 'Authorization: service xxx'"
    print(result)
    f = open('./'+str(sys.argv[2])+'.txt','a')
    f.write('\n')
    f.write(result)
    f.close()
    return

workbook = xlrd.open_workbook(str(sys.argv[1]))
print(workbook.sheet_names())
# 返现门槛
if "fxStage" in str(sys.argv[2]):
    sheet1 = workbook.sheet_by_name("返现门槛")
# 返现金额
elif "fxMoney" in str(sys.argv[2]):
    sheet1 = workbook.sheet_by_name("返现金额")
# 账单金额
elif "billMoney" in str(sys.argv[2]):
    sheet1 = workbook.sheet_by_name("账单金额")
# 最近一次返现金额
elif "lastRepay" in str(sys.argv[2]):
    sheet1 = workbook.sheet_by_name("返现金额")

ss = ''
for i in range(1,sheet1.nrows):
    # 用户ID，注意与excel文件中对比 double check
    ss += str(int(sheet1.cell(i,0).value))
    ss += '^^^'
    # 金额
    if ("fxMoney" in str(sys.argv[2])) or ("lastRepay" in str(sys.argv[2])):
        ss += str(sheet1.cell(i,1).value)
    else:
        ss += str(int(sheet1.cell(i, 1).value))
    if (i % 5)==0:
        printOut(ss)
        ss = ''
        continue
    ss += '~~~'
printOut(ss[:-3])

