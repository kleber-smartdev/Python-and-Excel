#Using openpyxl to import library workbook
from openpyxl import workbook, load_workbook

#Using workbook library to import xls file to a variable
workBookVariable = load_workbook('Grades.xlsx')

#Create a variable getting the active tab on xls file
workSheetVariable = workBookVariable.active

#Doing a loop with line
for cell in workSheetVariable['C']:
    print(cell.value)

#Doing a loop in the columm
for cell in workSheetVariable['3']:
    print(cell.value)