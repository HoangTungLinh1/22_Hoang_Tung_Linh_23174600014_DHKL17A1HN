import pandas as pd

ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

xep_theo_chieu_doc=pd.DataFrame({'ser1': ser1,'ser2': ser2}).T
print(xep_theo_chieu_doc)

xep_theo_chieu_ngang= pd.DataFrame({'ser1': ser1, 'ser2': ser2})
print(xep_theo_chieu_ngang)