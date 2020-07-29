from collections import Counter


str1 = Counter(input())
str2 = Counter(input())

if str1 == str2:
    print(1)
else:
    print(0)
print(int(str1 == str2))
