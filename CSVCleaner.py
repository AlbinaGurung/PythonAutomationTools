#Spreadsheet cleaner/CSV Cleaner
import pandas as pd
import numpy as np
file_path=("/Users/albinagurung/Desktop/Grade4.xlsx")

#print pandas version
print(pd.__version__)

#read excel file using pd
df=pd.read_excel(file_path,engine="openpyxl")
print(df.head())

# Replace empty strings or spaces with NaN
df = df.replace(r'^\s*$', np.nan, regex=True)

# Trim spaces in text columns
str_cols = df.select_dtypes(include="object").columns
df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

def drop_duplicate_columns(df):
    cols_to_drop=[]
    seen={}
    for col in df.columns:
        base_col = col.split(".")[0]  # Get the "base" name before pandas adds .1, .2 etc.
        if base_col not in seen:
            seen[col]=col
        else:
            if df[col].isna().all():
                cols_to_drop.append(col)
    df=df.drop(columns=cols_to_drop)
    print(seen)
    return df
df=drop_duplicate_columns(df)

#remove completely empty rows
clean_data=df.dropna(how="all") 
#how="all" means only remove columns where every cell is empty.

#remove completely empty columns
clean_data=df.dropna(axis=1,how="all") #axis=1 means columns.

#remove duplicates
clean_data=df.drop_duplicates()

#save cleaned file
clean_data.to_excel("cleaned_data.xlsx",index=False)
print("Data cleaned and saved as cleaned_data.xlsx")
print(clean_data.head())

# What not in seen means
# seen is a Python dictionary.
 # col not in seen checks if this column name has already been encountered while looping through all columns.