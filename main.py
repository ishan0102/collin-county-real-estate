import pandas as pd
import csv
import os

# load CSV files into dataframes
df_owner_info = pd.read_csv('data/raw_csv/owner_info.csv')
df_owner_taxes = pd.read_csv('data/raw_csv/owner_taxes.csv')

# filter dataframe
df_delinquent_taxes = df_owner_taxes[(df_owner_taxes['delinquency_date'] != '01/01/9999') # delinquency date is not null
                                   & (df_owner_taxes['bankruptcy_date'] != '01/01/9999') # bankruptcy date is not null
                                   & (df_owner_taxes['amount_due'].astype(float) >= 500.00)] # owes more than $500 in property taxes

# sort by most recent year
df_delinquent_taxes = df_delinquent_taxes.sort_values('year', ascending=False)

# filter for delinquent owner information
delinquent_account_numbers = df_delinquent_taxes['account_number'].tolist()
df_delinquent_owners = df_owner_info[df_owner_info['account_number'].isin(delinquent_account_numbers)]

# remove old CSV files if they already exist
try:
    os.remove('data/filtered_csv/delinquent_owner_info.csv')
    os.remove('data/filtered_csv/delinquent_owner_taxes.csv')
    print("The old owner_info.csv and owner_taxes.csv files have been removed.\n")
except:
    print("The files don\'t exist yet. They will be created automatically.\n")

# write dataframes to CSV files
print("Loading delinquent_owner_info.csv...")
df_delinquent_owners.to_csv('data/filtered_csv/delinquent_owner_info.csv', index=False)
print("Success!\n")

print("Loading delinquent_owner_taxes.csv...")
df_delinquent_taxes.to_csv('data/filtered_csv/delinquent_owner_taxes.csv', index=False)
print("Success!")
