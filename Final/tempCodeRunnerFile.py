n = int(input())
li = list(map(int, input().split()))
count = 0

for i in li:
    while i % 2 == 0:
        count += 1
        i /= 2
print(count)