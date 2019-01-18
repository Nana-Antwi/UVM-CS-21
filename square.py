#program the squares the numbers contained in a list

list1 = [1,5,6,7,8,12,14,15,18,20]
i = 0
while 1 < len(list1):
	list1[i] = list1[i] * list1[i]
	i += 1
print(list1[2:8])