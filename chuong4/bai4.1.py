import numpy as np
import pandas as pd
mylist= list('abceffghjklmnopqrstuvwxyz')
myarr=np.arange(26)
mydict=dict(zip(mylist, myarr))

print(pd.DataFrame(mylist, columns=['chu cai']))

print(pd.DataFrame(myarr, columns=['so']))

pdmydict= pd.Series(mydict)
print(pdmydict)
