import openpyxl
def get_value_excel(filename,cellname):
    wb=openpyxl.load_workbook(filename)
    Sheet1=wb['Trang_tính1']
    wb.close()
    return Sheet1[cellname].value
filename='input.xlsx'
cellname='A3'
x=get_value_excel(filename,cellname)
print(x)