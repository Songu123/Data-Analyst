students = [161,182,161,154,176,170,167,171,170,174,150,142,148,165,170,178,156,145,149,
 163,162,159,165,165,170,180,155,159,155,153,152,162,180,168,169,168,167,170]

print("Lop co so hoc sinh: ", len(students))
print("Chieu cao trung binh cua lop: ", sum(students) / len(students))
new_students = set(students)


print("Chieu cao cua cac hoc sinh: ", new_students)
print("Chieu cao trung bình của lớp: ", sum(new_students) / len(new_students))