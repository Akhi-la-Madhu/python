file1=open('file1.txt','r')
file2=open('file2.txt','w')
lines=file1.readlines()
type(lines)
for i in range(0,len(lines)):
    if(i%2):
        file2.write(lines[i])
file1=open('file1.txt','r')
file2=open('file2.txt','r')
str1=file1.read()
str2=file2.read()
print(str1)
print()
print("file2 content...")
print(str2)
file1.close()
file2.close()
        
