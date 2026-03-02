# Basic but doing it for the sake of complicity :P

#1 What is 5 to the power of 5?
print(5**5)

#2 What is the remainder from dividing 73 by 6?
print(73%6)

#3 How many times does the whole number 3 go into 123? What is the remainder of dividing 123 by 3?
print(123//3)
print(123%3)

#4 Split the following string into a list by splitting on the space character:
s = "MDS is going virtual!"
print(s.split())

#5 Given the below variables use f-strings to print:
# The speed of light is 2.997925e+08 m/s.

thing = "light"
speed = 299792458  # m/s

print(f"The speed of {thing} is {speed}")

#6 Given this nested list, use indexing to grab the word “MDS”:
l = [10, [3, 4], [5, [100, 200, ["MDS"]], 23, 11], 1, 7]

print(l[2][1][2])

#7 Given this nest dictionary grab the word “MDS”:
d = {
    "outer": [
        1,
        2,
        3,
        {"inner": ["this", "is", "inception", {"inner_inner": [1, 2, 3, "MDS"]}]},
    ]
}

print(d["outer"][3]["inner"][3]["inner_inner"][3])

#8 Why does the following cell return an error?

# t = (1, 2, 3, 4, 5)
# t[-1] = 6

# Because it's a tuple and tuples are immutable

#9 Use string methods to extract the website domain from an email, e.g., from the string "tomas.beuzen@fakemail.com", 
# you should extract "fakemail".
email = "tomas.beuzen@fakemail.com"
print(email[13:21])

#10 Given the variable language which contains a string, use if/elif/else to write a program that:
    # return “I love snakes!” if language is "python" (any kind of capitalization)
    # return “Are you a pirate?” if language is "R" (any kind of capitalization)
    # else return “What is language?” if language is anything else.

language = "python"

if language.lower() == "python":
    print("I love snakes!")
elif language.upper() == "R":
    print("Are you a pirate?")
else:
    print(f"What is {language}?")