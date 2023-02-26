lst = [[1, 2], [3, 4]]
#print(lst[1], lst[0])
for i in lst:
    print(lst[::-1])
print(lst["|".join(str(i[::-1])))