
# get all values by row for sheet "SPARES-FEMS"
def return_sp_fems(sheet_obj, row, column):
    for i in range(1, row + 1):
        none_counter = 0
        cell_obj = sheet_obj.cell(row=i, column=1)
        cell_obj2 = sheet_obj.cell(row=i, column=11)
        if cell_obj.value != None or cell_obj2.value != None:
            print(str(cell_obj.value).upper()+" - "+str(cell_obj2.value))
        
        if cell_obj.value == None:
            none_counter += 1
            if none_counter > 5 :
                pass


# get all values by row for sheet "TMX-ENV"
def return_env(sheet_obj, row, column):
    for i in range(1, row + 1):
        none_counter = 0
        cell_obj = sheet_obj.cell(row=i, column=1)
        cell_obj2 = sheet_obj.cell(row=i, column=4)
        if cell_obj.value != None or cell_obj2.value != None:
            print(str(cell_obj.value).upper()+" - "+str(cell_obj2.value))
        
        if cell_obj.value == None:
            none_counter += 1
            if none_counter > 5 :
                pass


# get all values by row for sheet "TMX-PHD"
def return_phd(sheet_obj, row, column):
    for i in range(1, row + 1):
        none_counter = 0
        cell_obj = sheet_obj.cell(row=i, column=1)
        cell_obj2 = sheet_obj.cell(row=i, column=8)
        if cell_obj.value != None or cell_obj2.value != None:
            print(str(cell_obj.value).upper()+" - "+str(cell_obj2.value))
        
        if cell_obj.value == None:
            none_counter += 1
            if none_counter > 5 :
                pass





# if sheet_obj.title == "TMX-WWS":
#         return_wws()


# get the active sheet object
# for sheet in sheets:
#     wb_obj.active = wb_obj.sheetnames.index(sheet)
#     sheet_obj = wb_obj.active
#     if sheet_obj.title == "TMX-WWS":
#         return_wws()        

#     row = sheet_obj.max_row
#     column = sheet_obj.max_column
    # return_wws()
    # return_sp_fems()
    # return_env()
    # return_phd()


# print("Rows : ", row)
# print("Column : ", column)





    # if sheet_obj.cell(row=i, column=11).value == None:
    #     sheet_obj.cell(row=i, column=11).value = "Hello Excel"






################################################################

# Save all to new excel file
# wb_obj.save("Sample.xlsx")


    # print(cell_obj.value)

# cell_obj = sheet_obj.cell(row=1, column=1)

# print(cell_obj.value)




# for row in sheet_obj.iter_rows(min_row=1, min_col=1, max_row=rowx+1, max_col=columnx+1):
#     for cell in row:
#         print(cell.value, end=" ")  
#     print()  