import pandas as pd
import sqlalchemy as db
orders_table = '../Chapter_4/H+ Sport orders.xlsx'
engine = db.create_engine('postgresql://postgres.xbmbtxticqvminmepvui:Ju_pi2BuadEG7xN@aws-0-us-east-1.pooler.supabase.com:6543/postgres')

def main():
  orders = pd.read_excel(orders_table, sheet_name='data')
  
  orders = orders[['OrderID', "Date", "TotalDue", "Status", "CustomerID", "SalespersonID"]]

  orders.to_sql('orders',engine, if_exists="replace", index=False)

  print('ETL script executed successfully')

