import numpy as np 
# noob way to solve this question 

prices = [100,200,300]
final_li = []
dis = 20
for price in prices:
    price_all = price - (price * dis / 100)
    final_li.append(price_all)

print(final_li)



# ultra pro max is here bro 

prices = np.array([100, 200, 300])
discount = 20
wizard = prices - (prices * discount / 100)
print(wizard)
