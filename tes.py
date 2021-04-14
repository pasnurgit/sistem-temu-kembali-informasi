import pandas as pd
import copy


ud1 = 5
ud2 = 2
ud3 = 1

data = {"stmik" : {"d1":2, "d2":5}, "akba" : {"d1":1, "d2": 2}, "makassar" : {"d1":2, "d3":5}}
tf = copy.deepcopy(data)

for term in data:
    for dok in data[term]:
        tf[term][dok] = data[term][dok] / ud1

df = pd.DataFrame(tf)
print(df.transpose())