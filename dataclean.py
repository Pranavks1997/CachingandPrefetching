import pandas as pd
from tabulate import tabulate
data = pd.read_csv('dataset.txt',header = None, sep=' ')
print(tabulate(data,showindex=False))
#data.style.set_properties(**{'text-align':'right'})
#print (data[[2,3]])