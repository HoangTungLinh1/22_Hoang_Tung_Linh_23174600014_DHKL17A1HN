import pandas as pd

emails = pd.Series([
    'buying books at amazom.com',
    'rameses@egypt.com',
    'matt@t.co',
    'narendra@modi.com'
])

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'

mail_hop_le = emails[emails.str.contains(pattern, regex=True)]
print(mail_hop_le)
