import pandas as pd

# load CSV files into dataframes
df_owner_info = pd.read_csv('data/csv/owner_info.csv')
df_owner_taxes = pd.read_csv('data/csv/owner_taxes.csv')

# filter dataframe
df_delinquent = df_owner_taxes.loc[(df_owner_taxes['delinquency_date'] != '01/01/9999') # delinquency date is not null
                               & (df_owner_taxes['bankruptcy_date'] != '01/01/9999') # bankruptcy date is not null
                               & (df_owner_taxes['amount_due'].astype(float) > 1000.00)] # owes more than $1000 in property taxes

# sort by most recent year
df_delinquent = df_delinquent.sort_values('year', ascending=False)

print(df_delinquent)
