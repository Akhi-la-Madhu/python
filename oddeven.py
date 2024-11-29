def num(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
a=int(input("enter a number"));
if(a>=1):
    print(num(a))
