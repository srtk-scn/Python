from pandas import DataFrame
import pandas as pd
filename= r"F:\Book1.xlsx"
df=pd.read_excel(filename)

InventoryID=[]
InventoryID=list(df['owl'])
print(InventoryID)
