import numpy as np

vec1 = np.arange(2,21,2)

vec2 = np.linspace(0,1,10)

vec_sum = vec1 + vec2
vec_prod = vec1 * vec2

vec_sqrt = np.sqrt(vec1)
print("sum:",vec_sum)
print("nhan:",vec_prod)

print("vec_sqrt:", vec_sqrt)
print("\nCăn bậc hai vec1:", vec_sqrt, vec_sqrt.shape, vec_sqrt.dtype)
print(vec1)
print(vec2)