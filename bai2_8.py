import math

so_nguyen_to = []
for i in range(10, 99):
    for j in range(2, int(math.sqrt(i))):
        if i % j == 0:
            break
        else:
            so_nguyen_to.append(i)
            break
print("Cac so nguyen to tu 10 den 99 la: ", so_nguyen_to)

def reverse(n):
    return int(str(n)[::-1])

so_nguyen_to_new = []
for i in so_nguyen_to:
    if i == reverse(i):
        so_nguyen_to_new.append(i)

print("Cac so nguyen to tu 10 den 99 la: ", so_nguyen_to_new)
