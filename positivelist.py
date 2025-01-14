list1=[]
list2=[]
n=int(input("Enter the limit:"))
print("Enter % d integers:"%n)
for i in range(0,n):
    a=int(input())
    list1.append(a)
print("List of integers:",list1)
for i in range(0,n):
    if list1[i]>0:
        b=list1[i]
        list2.append(b)
print("List of positive integers:",list2)        
