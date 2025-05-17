list_int = [3,6,2,5,4,1,10,4,2,5,6,11,325,234]

list_new = []

for i in range(len(list_int)):
    if list_int[i] % 2 == 0 and list_int[i] > 10:
        list_new.append(list_int[i])

print("List of even numbers greater than 10: ", list_new)