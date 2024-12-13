a = [2,4,6,8,10,12,16,23]
target = int(input())
for i in range(len(a)):
    if a[i] == target:
        print(i)