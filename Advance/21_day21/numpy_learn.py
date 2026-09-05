a = [1, 2]
b = [3, 4]

# Addition
# print(a + b) # [1, 2, 3, 4]

# Scalar multiplication
# print(a * 2) # [1, 2, 1, 2]

import numpy as np

arr_a = np.array([1, 2])
arr_b = np.array([3, 4])

# Matrix addition
# print(arr_a + arr_b)

# Scalar multiplication
# print(arr_b * 10)

# Dot product
# (1 * 3) + (2 * 4) = 3 + 8 = 11
# a · b = Σ(a_i * b_i) [from i=1 to n] = a_1*b_1 + a_2*b_2 + ... + a_n*b_n
"""       n
a · b = ∑ aᵢbᵢ = a₁b₁ + a₂b₂ + ... + aₙbₙ
"""
# print(np.dot(arr_a, arr_b)) # 11

# Vector magnitude
# print(np.linalg.norm(arr_a))

# Finding top match
similarities = np.array([0.12, 0.89, 0.91, 0.76])
best_idx = np.argmax(similarities)
# print(best_idx)
# print(similarities[best_idx])

def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    a = np.array(vec_a)
    b = np.array(vec_b)

    dot_product = np.dot(a, b)

    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if norm_a == 0 or norm_b == 0:
        return 0

    return float(dot_product / (norm_a * norm_b))


print(cosine_similarity([0.0, 1.0], [0.0, 1.0]))

