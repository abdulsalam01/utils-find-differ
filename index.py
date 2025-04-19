import numpy as np
import pandas as pd

# find difference between 2 datasets/files
# with different size / total data of files/datasets
# make sure: use fileNew as the data that has many data than file parameter
# len(fileNew) > len(file)
# column need to be exists in fileNew data
# idx has to be number
def see_differ(file, fileNew, column, idx):
    sheet1, sheet2 = None, None
    with file as reader1, fileNew as reader2:
        sheet1 = pd.read_excel(reader1)
        sheet2 = pd.read_excel(reader2)

    sheet3 = []
    to_arr = sheet1.to_numpy()
    for id in sheet2[column]:
        if id not in to_arr[:, idx]:
            sheet3.append(id)

    diff = sheet2[sheet2[column].isin(sheet3)]
    return diff

# 
# EXAMPLE TO USE
path_excel = ""
path_file = "output-july_new-6.xlsx"
file = pd.ExcelFile(path_excel + path_file)
fileNew = pd.ExcelFile(path_excel + "FINAL_DPL_KM4.xlsx")
# attach file parameter as file that want to be compared with fileNew(the master file, the lookup one)
# check what column that we want to be see the differ
# at which index the file parameter (1st parameter) has the same value with column parameter
diff_sd = see_differ(file=file, fileNew=fileNew, column="NIDN", idx=4)
# export the difference to excel
diff_sd.to_excel(path_excel + 'residue_new_dosen_from_output_july_km4.xlsx')