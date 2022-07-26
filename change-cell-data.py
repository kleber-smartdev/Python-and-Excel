from openpyxl import workbook, load_workbook
workBookVariable = load_workbook('Grades.xlsx')
workSheetVariable = workBookVariable.active
workSheetVariable['A2'] = "Hat"
workBookVariable.save('Grades.xlsx')