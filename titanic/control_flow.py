x = -2
if x > 0:
    print("x is possitive")
elif x < 0:
    print("x is nagitive")
else:
    print("x is zero")
food = ["list", "string list", "not food"]
i = 0
while i <6:
    i+=1
    if i==3:
        continue
    print(i)
for foo in food:
    print(foo)
    for f in foo:
        print(f)

def user_input(n):
    if n ==1:
        return 1
    else :
        return n*user_input(n-1)
print(user_input(3) )  
x = lambda a: +1
import pandas as pd
import math
print(math.sqrt(9))