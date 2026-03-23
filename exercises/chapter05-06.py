#1 Import numpy under the alias np.

import numpy as np

#2 Create the following arrays:
# Create an array of 5 zeros.
# Create an array of 10 ones.
# Create an array of 5 3.141s.
# Create an array of the integers 1 to 20.
# Create a 5 x 5 matrix of ones with a dtype int.

print(np.zeros(5))
print(np.ones(10))
print(np.full(5, 3.141))
print(np.array(range(21)))
print(np.ones((5, 5), dtype=int))

#3 Use numpy to:
# Create an 3D matrix of 3 x 3 x 3 full of random numbers drawn from a standard normal distribution (hint: np.random.randn())
# Reshape the above array into shape (27,)
md3 = np.random.randn(3, 3, 3)

print(md3)

print(md3.reshape(27,))

#4 Create an array of 20 linearly spaced numbers between 1 and 10.
print(np.linspace(1, 10, 20))

#5 Run the following code to create an array of shape 4 x 4 and then use indexing to produce the outputs shown below.

a = np.arange(1, 26).reshape(5, -1)

print(a)

print(a[3, 4])

print(a[1:, 3:])

print(a[1, :])

print(a[2:4])

print(a[1:3, 2:4])

#6 Calculate the sum of all the numbers in a.
print(a.sum())
print(np.sum(a))    # accidently found out you can do like this as well

#7 Calculate the sum of each row in a.
print(a.sum(axis=1))

#8 Extract all values of a greater than the mean of a (hint: use a boolean mask).
print(a[a > a.mean()])

#9 Find the location of the minimum value in the following array b:
np.random.seed(123)
b = np.random.randn(10)
print(b)

print(np.min(b))    # this gives the value
print(b.argmin())   # this gives the location

#10 Find the location of the maximum value in the following 2D array c 
np.random.seed(123)
c = np.random.randn(3, 2)
print(c)

print(c.argmax())