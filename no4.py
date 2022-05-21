x=[1,2,3,4,5,6,7,8]
def max(x):
    max=x[0]
    for i in x:
        if i>max:
            max=i
    return max
print(max(x))
    