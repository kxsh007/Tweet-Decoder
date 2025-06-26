import numpy as np
import math

temperature = 45
weather = "sunny"

print("""
> "The current temperature in my city is {} degrees Celsius and the weather is {}."
""".format(temperature, weather))
mixed_data_types = [1, 2.5, "hello", True, [1, 2, 3]]
data_types = [type(element) for element in mixed_data_types]
data_types
r = 5
area = math.pi* (r**2)
n = 576
sq_root = math.sqrt(n)
area, sq_root
lyrics = """It was the best of times, it was the worst of times, it was the age of wisdom,it was the age of foolishness,it was the epoch of belief,it was the epoch of incredulity,it was the season of Light, it was the season of Darkness, it was the spring of hope,it was the winter of despair,"""
count1 = lyrics.count("the")
count2 = lyrics.count("epoch")

count1, count2
# Get the number from the user
number = int(input("Enter a number: "))

# Check if the number is divisible by both 2 and 3
is_divisible_by_2_and_3 = (number%2 == 0) and (number%3 == 0)

# Print the result
if is_divisible_by_2_and_3:
    print(f"{number} is divisible by both 2 and 3.")
else:
    print(f"{number} is not divisible by both 2 and 3.")
r1=10-5
r2=7*2
if r1>r2:
  print("the result of (10-5) is greater than (7*2)")
if r1==r2:
  print("the result of (10-5) is equal to (7*2)")
def find_intersection(list1, list2):
    """
    Find the intersection of two lists.

    Parameters:
    - list1: The first list.
    - list2: The second list.

    Returns:
    - intersection: A list containing the common elements between list1 and list2.
    """
    intersection = [item for item in list1 if item in list2]

    return intersection
    # Test the function with the given lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print("Intersection:", find_intersection(list1, list2))
def grade(scores):
    results = []
    for score in scores:
        if score > 60:
            results.append("Pass")
        else:
            results.append("Fail")
    return results
scores = [75, 45, 80, 30, 65]
print("Grading Results:", grade(scores))
i = 10
while i >= 1:
  print(i)
  i=i-1
  def sum_list(mylist):
    return sum(mylist)
mylist = [1, 2, 3, 4, 5]
print("Sum of mylist:", sum_list(mylist))
print(" Yes, functions can be called inside another function.It is known as function composition")
print("Yes, a function can call itself. This is known as recursion.")
print("No, variables defined inside a function are local to that function and cannot be accessed directly by another function. This is known as local scope. However, you can return a value from one function and pass it to another.")
