k = []


for i in range(0, 10):
    k.append(i)

for key in k:
    print(key, k[key])



print(k)
for i in range(0,len(k)):
    print(i,k[i])

length = len(k)
i = 0
while i <= length - 5:
    k.remove(i)
    print(len(k))
    i = i + 1