#import openpyxl
from utilities import XLUtils
import os

# testDataFolder = os.path.join(os.path.abspath(os.curdir),"testData")
# if not os.path.exists(testDataFolder):
#     os.makedirs(testDataFolder)
# file = os.path.join(testDataFolder,"Automation_Exercise_LoginData.xlsx")
#file = os.path.abspath(os.curdir)+"\\testData\\Automation_Exercise_LoginData.xlsx"

cur_script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(cur_script_dir)
file = os.path.join(project_root, 'testData', 'Automation_Exercise_LoginData.xlsx')
sheetName = "Sheet1"
rows = XLUtils.getRowCount(file, sheetName)
cols = XLUtils.getColumnCount(file, sheetName)

XLUtils.writeData(file, sheetName, 1,1,"username")
XLUtils.writeData(file, sheetName, 1,2,"password")
XLUtils.writeData(file, sheetName, 1,3,"res")

XLUtils.writeData(file, sheetName, 2,1,"abc2005@gmail.com")
XLUtils.writeData(file, sheetName, 2,2,"12345678")
XLUtils.writeData(file, sheetName, 2,3,"Valid")

XLUtils.writeData(file, sheetName, 3,1,"abc2005@gmail.com")
XLUtils.writeData(file, sheetName, 3,2,"test")
XLUtils.writeData(file, sheetName, 3,3,"Invalid")

XLUtils.writeData(file, sheetName, 4,1,"abc1232005@gmail.com")
XLUtils.writeData(file, sheetName, 4,2,"12345678")
XLUtils.writeData(file, sheetName, 4,3,"Invalid")

XLUtils.writeData(file, sheetName, 5,1,"abc@gmail.com")
XLUtils.writeData(file, sheetName, 5,2,"123456789")
XLUtils.writeData(file, sheetName, 5,3,"Invalid")

for r in range(1,rows+1):
    for c in range(1,cols+1):
        print(XLUtils.readData(file,sheetName,r,c), end = '   ')
    print()

#print(XLUtils.readData(file, sheetName, 5,2))
#print(rows)