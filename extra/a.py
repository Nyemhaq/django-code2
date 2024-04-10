n = int(input())
li = list(map(int, input().split()))

count = 0
li_2 = []
for i in li:
    while (i % 2 ==0):
        count += 1
        i /= 2
    li_2.append(count)
    count = 0
# print(li_2)
print(min(li_2))
    



from collections import Counter

n = int(input())
li = list(map(int, input().split()))

count_li = Counter(li)

tot_val = 0

for val, cnt in count_li.items():
    if cnt > val:
        tot_val += cnt - val
    elif cnt < val:
        tot_val += cnt

print(tot_val)

    
