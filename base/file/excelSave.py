from openpyxl import Workbook


wb = Workbook()
wb.create_sheet('Data', index=1)
sheets = wb.get_sheet_names()
sheet = wb.get_sheet_by_name(sheets[0])
sheet['A1'] = 'good'
sheet['B1'] = 'hello'
# sheet.index('A1','good')
wb.save(r'./example.xlsx')