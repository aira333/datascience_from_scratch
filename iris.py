# testing a perceprtorn on the iris dataset

# using two flowers from the iris dataset - Iris Setosa and Iris Versicolor

import os
import pandas as pd
s =  'https://archive.ics.uci.edu/ml/'\
     'machine-learning-databases/iris/iris.data'
     
print('URL:', s)

df = pd.read_csv(s, header=None, encoding='utf-8')
df.tail()

