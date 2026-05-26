n = [11,2,7,15]
ind = []
for i in range(0,len(n)):
    for j in n :
        if n[i] + j == 9 :
            ind += [i]
print(f"index of two items {ind}")
