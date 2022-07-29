import xlrd

data = xlrd.open_workbook("ArmorNameList1.xls")
table = data.sheets()[0]
ArmorDir = {}
for i in range(0, 572):
    table_list = table.row_values(rowx=i, start_colx=0, end_colx=None)
    ArmorDir[table_list[0]] = table_list[1]

print(len(ArmorDir))
print(ArmorDir)

if ArmorDir["dqwd"]:
    print("true")
else:
    print("f")