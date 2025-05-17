import numpy as np

names = np.array(['An', 'Binh', 'Cuong',
 'An', 'Dung', 'Binh', 'Binh'])

scores = np.random.randint(50, 101, size=(7,3))

print("Student Names: ", names)
print("Scores:\n", scores)

is_binh = (names == 'Binh')
print("\nCondition (names == 'Binh'):", is_binh)

scores[is_binh] = -1 # Gán -1 cho cả hàng tương ứng
print("\nAfter assigning -1 to scores of 'Binh':\n", scores)