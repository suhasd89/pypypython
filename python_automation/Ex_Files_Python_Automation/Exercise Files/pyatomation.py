f = open('inputFile.txt','r')
#print(f.read())
count=0
for line in f:
    if 'P' in line:
        print(count,line)
        count += 1
f.close()
print('number of student pass is',count)