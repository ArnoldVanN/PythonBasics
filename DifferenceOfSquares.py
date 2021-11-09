sum = 0
sums_squared = 0
for x in range(1, 11):
    sum += x
sums_squared = sum**2
print("Sum of first 10 natural numbers squared: ", sums_squared)
sum = 0
for x in range(1, 11):
    sum += x**2
print("Sum of squares of first 10 natural numbers: ", sum)
print("Difference between square of the sum and sum of the squares is:", sums_squared - sum)