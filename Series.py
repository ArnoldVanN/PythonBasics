digits = input()
K = 3
# Extract K length substrings
# Using list comprehension + string slicing
res = [digits[i: j] for i in range(len(digits)) for j in range(i + 1, len(digits) + 1) if len(digits[i:j]) == K]
  
print("All K length substrings of string are : " + str(res))