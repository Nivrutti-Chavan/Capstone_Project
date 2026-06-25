import pandas as pd
import numpy as np

data=pd.read_csv("Airbnb_Open_Data.csv")

colm_to_keep=['id', 'NAME', 'host id', 'host_identity_verified', 'host name',
       'neighbourhood group', 'neighbourhood', 'lat', 'long', 'country',
       'country code', 'instant_bookable', 'cancellation_policy', 'room type',
       'Construction year', 'price', 'service fee', 'minimum nights',
       'number of reviews', 'last review']


colm_to_drop=['reviews per month',
       'review rate number', 'calculated host listings count',
       'availability 365', 'house_rules', 'license']
print(data.shape)
#droping unnecesarry column
data.drop(columns=colm_to_drop,inplace=True)

#reaname of colm
data.rename(columns={"NAME":"Name"},inplace=True)

for_lower=[]
for i in data.columns:
   for_lower.append(i.lower())
print(for_lower)

for_upper=[]
for x in data.columns:
    for_upper.append(x.upper())
print(for_upper)

#Droping duplicates
print(data.duplicated().value_counts()) #show count of unique and duplicates values 
print(data.duplicated().sum())#show only duplicate values in boolean format true means duplicates 

remove_duplicates=data.drop_duplicates(inplace=True)

print(data.duplicated().sum())

#removing nan values
data.drop(columns=["last review"],inplace=True)
data.dropna(inplace=True)
print(data.isna().sum())
print(data)

data.to_excel("new_data.xlsx",index=False)