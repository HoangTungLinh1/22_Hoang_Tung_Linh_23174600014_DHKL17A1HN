import pandas as pd

stocks1 = pd.read_csv('chuong4\stocks1.csv')
stocks2 = pd.read_csv('chuong4\stocks2.csv')
companies = pd.read_csv('chuong4\companies.csv')

print(stocks1.info())
print(stocks2.info())
print(companies.info())

stocks1.fillna({'high': stocks1['high'].max(), 'low': stocks1['low'].min()}, inplace=True)

stocks = pd.concat([stocks1, stocks2])
print(stocks.head(15))

stocks_companies = stocks.merge(companies, left_on='symbol', right_on='name')
print(stocks_companies.head())

stocks_companies['parsed_time'] = pd.to_datetime(stocks_companies['date'])
print(stocks_companies['parsed_time'].dtype)

stocks_companies['result'] = stocks_companies['close'] > stocks_companies['open']
stocks_companies['result'] = stocks_companies['result'].replace({True: 'up', False: 'down'})
print(stocks_companies[['symbol', 'result']])
