#COPY A TEXT FILE TO ANOTHER FILE

'''file1=input("Enter the source file to be copied:")
file2=input("Enter the destination file name:")
fr=open(file1,"r")
fw=open(file2,"w")
for line in fr.readlines():
    fw.write(line)
fr.close()
fw.close()
print("1 file copied")'''

#COUNT THE NUMBER OF LINES IN A FILE

'''a=open("source.txt","r")
countlines=0
for line in a.readlines():
    countlines=countlines+1
print("Number of lines:",countlines)
a.close()'''


#COUNT THE FREQUENCIES OF EACH WORD FROM A FILE

b = open("source.txt","r")
wordcount = {}
for word in b.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print(k,v)        
b.close()    
