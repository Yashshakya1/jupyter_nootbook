import pandas as pd 
data = {
"Name"  : ['yash','yash vardhan','tanya','tushi','mohit','monu','shinchan','nobitha','doremone'],
"age"   : [21,23,20,18,25,26,45,22,30],   # Note: these are strings, not numbers
"salary":[101000,100000,10000,20000,150,12000,15000,25000,30000],
"work"  : ['data science','data analyst','sales executive','accounted','swiper','hardware Engineering',
           'maneger','bank maneger','scientest']
}
df = pd.DataFrame(data)
print(df)
add = df.insert(2,"ghooo",[45,5,45,45,4,54,84,84,95])
print(df)
print("head and tail about 5 :- ")
print(df.head(2))
print(df.tail(2))
print("information of disc() and info()")
print(df.info())
print(df.describe())
print("shape and column attribute :- ")
print(df.shape)
print(df.columns)
print("update values by using loc() method :- ")
df.loc[2,"salary"] = 5
print(df)
# multicolumns update
df["salary"] = df["salary"] * 5.1
print(df)

# remove any columns 
df.drop(columns = ["age"] , inplace= True)
print(df)
df.drop(columns = ["salary","work"], inplace= True)
print(df)