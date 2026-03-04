#1 Create a function website() that grabs the website domain from a url string. 
# For example, if your function is passed "www.google.com", it should return "google".

def website(url):
    return url.split(".")[1]

print(website("www.google.com"))

#2 Create a function divisible(a, b) that accepts two integers (a and b) and returns True if a is divisble by b without a remainder. 
# For example, divisible(10, 3) should return False, while divisible(6, 3) should return True.

def divisible(a, b):
    if a%b==0:
        return True
    else:
        return False

print(divisible(6, 9))

#3 Use list comprehension to square every number in the following list of numbers.
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squared = [i**2 for i in l]
print(squared)

#4 For the following list of names, 
# write a list comprehension that creates a list of only words that start with a capital letter (hint: str.isupper()).

names = ['Steve Irwin', 'koala', 'kangaroo', 'Australia', 'Sydney', 'desert']

capt = [word for word in names if word[0].isupper()]
print(capt)

#5 For the following list of keys and vals use dictionary 
# comprehension to create a dictionary of the form {'key-0': 0, 'key-1': 1, etc} 
# (hint: zip() can help you combine two lists into on object to be used for comprehension/looping).

keys = [f"key-{k}" for k in range(10)]
vals = range(10)

print({k:v for k, v in zip(keys, vals)})

#6 Create a generator function called listgen(n) that yields numbers from 0 to n, in batches of lists of maximum 10 numbers at a time. 

def listgen(n):
    i = 0
    numbers = list(range(n))
    while i <= n // 10:
        yield numbers[10 * i:10*(i+1)]
        i += 1

#7 Write a try/except to catch the error generated from the following code and print “I caught you!”. 
# Make sure you catch the specific error being caused, this is typically better practice than just catching all errors!

try:
    5 / 0
except ZeroDivisionError:
    print("I caught you!")

#8 Create a function lucky_sum() that takes all the integers a user enters and returns their sum. 
# However, if one of the values is 13 then it does not count towards the sum, nor do any values to its right.

def lucky_sum(*args):
    if 13 in args:
        return sum(args[:args.index(13)])
    return sum(args)

print(lucky_sum(1,3,4,13,5))