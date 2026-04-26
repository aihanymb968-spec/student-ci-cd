numbers = [1, 2, 3, 4, 11, 7, 24]

list2 = [i * 2 for i in numbers]

taq = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]
jup = [list2[i] for i in range(len(list2)) if i % 2 == 0]

list3 = [taq[i] + jup[i] for i in range(len(taq))]

print("list1:", numbers)
print("list2:", list2)
print("list3:", list3)