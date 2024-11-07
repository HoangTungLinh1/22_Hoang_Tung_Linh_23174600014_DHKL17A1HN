import csv
import numpy as np

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
        return header, data

header1, stocks1 = read_csv_file('chuong3/stocks1.csv')

print("5 dòng đầu của stocks1:", stocks1[:5])
print("5 dòng cuối của stocks1:", stocks1[-5:])

dtypes = [type(value) for value in stocks1[0]]
print("Dtypes của stocks1:", dtypes)

print("Số lượng dòng và cột trong stocks1:", len(stocks1), len(header1))

header2, stocks2 = read_csv_file('chuong3/stocks2.csv')

print("5 dòng đầu của stocks2:", stocks2[:5])
print("5 dòng cuối của stocks2:", stocks2[-5:])

dtypes2 = [type(value) for value in stocks2[0]]
print("Dtypes của stocks2:", dtypes2)

print("Số lượng dòng và cột trong stocks2:", len(stocks2), len(header2))
header_companies, companies = read_csv_file('chuong3/companies.csv')

print("Dữ liệu của companies:", companies[:5])

dtypes_companies = [type(value) for value in companies[0]]
print("Dtypes của companies:", dtypes_companies)

print("Số lượng dòng và cột trong companies:", len(companies), len(header_companies))

def check_and_replace_null(data, header):
    for i, col in enumerate(header):
        column_data = [float(row[i]) if row[i] else None for row in data]
        if None in column_data:
            print(f"Phát hiện giá trị null trong cột {col}")

            if col == 'high':
                max_value = max([float(row[i]) for row in data if row[i]])
                for row in data:
                    if not row[i]:
                        row[i] = max_value
            elif col == 'low':
                min_value = min([float(row[i]) for row in data if row[i]])
                for row in data:
                    if not row[i]:
                        row[i] = min_value

check_and_replace_null(stocks1, header1)

stocks = np.vstack((stocks1, stocks2))

print("15 dòng cuối của stocks:")
print(stocks[-15:])

def join_stocks_and_companies(stocks, companies, stocks_header, companies_header):
    companies_dict = {row[0]: row[1:] for row in companies}  # Tạo dict từ companies dựa trên symbol
    merged_data = []
    for row in stocks:
        company_data = companies_dict.get(row[1], ['N/A'] * (len(companies_header) - 1))  # Tìm thông tin công ty theo symbol
        merged_data.append(row + company_data)
    return merged_data

stocks_companies = join_stocks_and_companies(stocks, companies, header1, header_companies)

print("5 dòng đầu của stocks_companies:")
print(stocks_companies[:5])

def calculate_mean_by_company(data, header, column_indices):
    company_means = {}
    for row in data:
        company = row[1]
        values = [float(row[i]) for i in column_indices]
        if company not in company_means:
            company_means[company] = []
        company_means[company].append(values)
    
    for company, values in company_means.items():
        mean_values = np.mean(values, axis=0)
        print(f"Trung bình giá trị cho {company}: {mean_values}")

open_idx, high_idx, low_idx, close_idx, volume_idx = [header1.index(col) for col in ['open', 'high', 'low', 'close', 'volume']]
calculate_mean_by_company(stocks, header1, [open_idx, high_idx, low_idx, close_idx, volume_idx])
from datetime import datetime

for row in stocks_companies:
    row.append(datetime.strptime(row[0], '%Y-%m-%d'))  # Chuyển date sang datetime

for row in stocks_companies:
    open_price = float(row[2])
    close_price = float(row[5])
    result = 'up' if close_price > open_price else 'down'
    row.append(result)

print("5 dòng đầu tiên của stocks_companies với parsed_time và result:")
print(stocks_companies[:5])
