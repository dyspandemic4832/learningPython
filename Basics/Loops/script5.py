count = 0

while(count < 5):
    print(count)
    count += 1
else:
    print("Value reached %d" %(count))

for i in range(1,10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print("Because condition in loop say so! break will break else")