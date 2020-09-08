"""
行合并

"""
import pandas as pd

data = [
    ['x1',1,'a'],
    ['x1',2,'c'],
    ['x2',1,'b'],
    ['x1',3,'b'],
    ['x2',2,'c'],
    ['x2',3,'a']
]
columns = ['people','order','route']

df = pd.DataFrame(data=data,columns=columns)
print(df)

df=df.sort_values(by=['people','order'],ascending=True)
res = df[['people','route']].groupby(['people'])\
	.apply(lambda x:"->".join(x['route'])).reset_index()
print(res)
