import numpy as np
import pandas as pd 
dis = {
     "name" : ["yash","suraj","rani","shinchan"],
     "age" :  [45,12,8,48],
     "number": [1246465,1231654,1216546,1261564]
}
df = pd.DataFrame(dis)
print(df)
print(df.transpose())