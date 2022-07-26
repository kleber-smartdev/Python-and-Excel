# import openpyxl
from openpyxl import workbook, load_workbook
workBookVariable = load_workbook('Grades.xlsx')
workSheetVariable = workBookVariable.active
print(workSheetVariable["A3"].value)