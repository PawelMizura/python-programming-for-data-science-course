# 1 Use flake8 to list all the syntatic and stylistic problems with the following code.

very_long_variable_name = {"field": 1, "is_debug": True}
if (
    very_long_variable_name is not None
    and very_long_variable_name["field"] > 0
    or very_long_variable_name["is_debug"]
):
    z = "hello " + "world"
else:
    f = rf"hello {world}"
if True:
    y = "hello " "world"  # FIXME: https://github.com/python/black/issues/26


class Foo(object):
    def f(self):
        return 37 * -2

    def g(self, x, y=42):
        return y


regular_formatting = [0, 1, 2, 3, 4, 5]


def CAPITALIZE(mystring):
    return mystring.upper()


# 2 Use black to autoformat the following code.

very_long_variable_name = {"field": 1, "is_debug": True}
if (
    very_long_variable_name is not None
    and very_long_variable_name["field"] > 0
    or very_long_variable_name["is_debug"]
):
    z = "hello " + "world"
else:
    f = rf"hello {world}"
if True:
    y = "hello " "world"  # FIXME: https://github.com/python/black/issues/26


class Foo(object):
    def f(self):
        return 37 * -2

    def g(self, x, y=42):
        return y


regular_formatting = [0, 1, 2, 3, 4, 5]


def CAPITALIZE(mystring):
    return mystring.upper()


# Output from the console:

# black exercises\chapter04.py 
# reformatted exercises\chapter04.py

# All done! ✨ 🍰 ✨
# 1 file reformatted.

#3 Import class circle here and answer the following:
# What is the area of a circle with radius 10?
# What is the circumference of a circle with radius 10?

from chapter03 import Circle
x = Circle(10)
print(f"Area of the circle: {x.area():.2f}")
print(f"Circumference of the circle: {x.circumference():.2f}")

#4 In this exercise I want you to create a function that models each guest’s attendance as a Bernoulli random variable.
# I’ve given you the list of probabilities to get you started. 
# Your code should output the total number of attendees after running your simulation.

probabilities = [1, 0.75, 0.5, 0.75, 0.5, 1, 0.5, 0.75]

import numpy as np

attendance = [np.random.binomial(n=1, p=p) for p in probabilities]
print(f"{sum(attendance)} guests arrived at the party")

#5 Now I want you to write a function that runs n simulations and returns a list of the total number of attendees for each simulation.
#  Calculate the average guest attendance after running 100 simulations (round up to the nearest integer - hint: math.ceil()).

import math

def simulate_party(probabilities, n):
    "Simulate attendance at a party from a list of attendance probabilities."
    attendance = []
    for i in range(n):
        attendance.append(sum([np.random.binomial(n=1, p=p) for p in probabilities]))
    return attendance


simulations = simulate_party(probabilities, 100)

print(
    f"Avg. number of guests across all simulations: {math.ceil(sum(simulations) / len(simulations))}"
)

# Use this code to plot your function on a bigger guest list!
import matplotlib.pyplot as plt
plt.style.use('ggplot')  # These lines are to do with plot formatting. We'll talk about them in a later chapter.
plt.rcParams.update({'font.size': 16, 'axes.labelweight': 'bold', 'figure.figsize': (8, 6)})

number_of_guests=100
probabilities = np.random.choice([0.2, 0.4, 0.6, 0.8, 1],
                                 size=number_of_guests,
                                 p=[0.1, 0.2, 0.2, 0.3, 0.2])
attendance = simulate_party(probabilities, n=1000)
plt.hist(attendance, bins=20)
plt.xlabel("Avg. number of attendees")
plt.ylabel("Number of simulations");