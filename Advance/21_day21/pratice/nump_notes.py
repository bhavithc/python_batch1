vec_a = [1, 2]
vec_b = [3, 4]


# Addition 
print(vec_a + vec_b) # 1, 2, 3, 4

# Scalar muliptication 
print(vec_a * 2) # 1, 2, 1, 2

# Element wise multiplication
result = []
for a, b in zip(vec_a, vec_b):
    result.append(a * b)
print(result) # [3, 8]


print("**" * 25)
print("Numpy way")
print("**" * 25)
# Numpy way of doing it 
import numpy as np
vec_c = np.array([1, 2])
vec_d = np.array([3, 4])

# 1. Addition 
print(vec_c + vec_d) # [4, 6]

# 2. Scalar multiplication
print(vec_c * 2) # [2, 4]

# 3. Elementwise multiplication
print(vec_c * vec_d) # [3, 8]

# 4. Dot product: multiplies matching components of two vectors and sums them up:
"""
       n
a · b = ∑ aᵢbᵢ = a₁b₁ + a₂b₂ + ... + aₙbₙ
"""
# a · b = Σ(a_i * b_i) [from i=1 to n] = a_1*b_1 + a_2*b_2 + ... + a_n*b_n
# (1 * 3) + (2 * 4) = 3 + 8 = 11
print(np.dot(vec_c, vec_d)) # 11

# 5. Vector Magnitude / L2 Norm (np.linalg.norm)
# The length (Euclidean magnitude or L2 norm) of a vector measures its geometric distance from the origin:
norm_c = np.linalg.norm(vec_c)
# calculation: sqrt(1 ^ 2 + 2 ^ 2) = sqrt(1 + 4) = sqrt(5) = 2.23
print(norm_c)

# 6. Finding the Top Match (np.argmax)
# np.argmax returns the index of the highest value in an array—crucial 
# for selecting the best document chunk in RAG.
similarities = np.array([0.12, 0.89, 0.45, 0.76])
best_idx = np.argmax(similarities)
print("Best index: ", best_idx) # 1 (index)
print("Highest score: ", similarities[best_idx]) # 0.89

# Cosine Similarity
# 1. Geometric Intuition
# Cosine similarity measures the direction (angle) between two vectors 
# rather than their magnitude (length).
# In text embeddings:
# - Direction encodes semantic meaning and topical content.
# - Magnitude often reflects document length or repetitive frequency.
# Cosine similarity answers: "Are these two pieces of text pointing toward the same concept?"

# Interpreting the Score Range
# Score | Angular Separation | Interpretation in Text Embeddings
# +1.0. | 0 deg.             | Identical direction / perfectly synonymous meaning
# > 0.0 | < 90 deg           | Positive semantic correlation / shared concepts
# 0.0   | 90 deg (orthogonal)| Unrelated topics / independent meanings
# < 0.0 | > 90 deg           | Opposing meanings (rare in positive embedding spaces)

def cosine_similarity(vec_e: list[float], vec_f: list[float]) -> float:
    # 1. Convert Python lists into optimized NumPy ndarrays
    a = np.array(vec_e)
    b = np.array(vec_f)

    # 2. Compute the numerator (dot product)
    dot_product = np.dot(a, b)

    # 3. Compute the denominator (product of vector lengths)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    # 4. Handle division by zero (edge case if vector is all zeros)
    if norm_a == 0 or norm_b == 0:
        return 0.0 

    return float(dot_product / (norm_a * norm_b))


# Example just to visualize 

# Query "biology class"
query = np.array([1.0, 0.0]) # "biology class"

# Doc 1: "photosynthesis and cells" (aligned direction)
doc_relevant = np.array([2.0, 0.5])

# Doc 2: "operating systems and C++" (perpendicular direction)
doc_irrelevant = np.array([0.1, 3.0])

print("Doc 1 Similarity:", cosine_similarity(query, doc_relevant))     # ~0.97 (High)
print("Doc 2 Similarity:", cosine_similarity(query, doc_irrelevant)) 