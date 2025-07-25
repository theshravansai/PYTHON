# # 1. Write a code to reverse a string.
a = "education"
reversed_string = a[::-1]
print(a)
print(reversed_string)


# 2. Write a code to count the number of vowels in a string.
s = "education"
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print(count)


# 3. Write a code to check if a given string is a palindrome or not.
s = "madam"
if s == s[::-1]:
    print("Palindrome hai")
else:
    print("Palindrome nahi hai")


# 4.Write a code to check if two given strings are anagrams of each other .
s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("Anagram hai")
else:
    print("Anagram nahi hai")


# 5.Write a code find all occurrences of given substring within another string.
text = "good hello nice"
sub = "hello"
index = 0
while index < len(text):
    index = text.find(sub, index)
    if index == -1:
        break
    print("Mila at index:", index)
    index += 1


# 6.Write a code to perform basic string compression using the counts of repeated characters.
s = "aaabbccc"
compressed = ""
i = 0
while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i+1]:
        count += 1
        i += 1
    compressed += s[i] + str(count)
    i += 1
print(compressed)


# 7.Write a code to determine if a string has all unique characters.
name = "fruit"
if len(set(name)) == len(name):
    print("Sab characters unique hain")
else:
    print("Kuch characters repeat ho rahe hain")


# 8.Write a code to convert a given string to uppercase or lowercase.
Fruit = "Mango"
print(Fruit.upper())
print(Fruit.lower())


# 9.Write a code to count the number of words in a string.
s = "This is my first assignment"
words = s.split()
print("Words:", len(words))


# 10.Write a code to concatenate two strings without using the + operator.
s1 = "Hello "
s2 = "World"
result = "{}{}".format(s1, s2)
print(result)


# 11.Write a code to remove all occurrences of a specific element from a list.
lst = [1, 2, 3, 2, 4, 2]
x = 2
new_list = [i for i in lst if i != x]
print(new_list)


# 12.Implement a code to find the second largest number in a given list of integers.
num = [10, 20, 4, 45, 99]
num = list(set(num))
num.sort()
print("Second Largest:", num[-2])


# 13.Create a code to count the occurrences of each element in a list and returna dictionary with elements as keys and their counts as values.
lst = [1, 2, 2, 3, 1]
count_dict = {}
for i in lst:
    count_dict[i] = count_dict.get(i, 0) + 1
print(count_dict)


# 14.Write a code to reverse a list in -place without using any built-in reverse functions.
lst = [1, 2, 3, 4]
for i in range(len(lst)//2):
    lst[i], lst[-i-1] = lst[-i-1], lst[i]
print(lst)


# 15.Implement a code to find and remove duplicates from list while preserving the original order of elements.
lst = [1, 2, 2, 3, 1]
seen = set()
result = []
for i in lst:
    if i not in seen:
        seen.add(i)
        result.append(i)
print(result)


# 16.Create a code to check if a given list is sorted (either in ascending order or descending order) or not.
lst = [1, 2, 3, 4]
if lst == sorted(lst) or lst == sorted(lst, reverse=True):
    print("Sorted hai")
else:
    print("Sorted nahi hai")


# 17.Write a code to merge two shorted lists into a single sorted list.
a = [1, 3, 5]
b = [2, 4, 6]
merged = sorted(a + b)
print(merged)


# 18.Implement a code to find the intersection of two given lists.
a = [1, 2, 3]
b = [2, 3, 4]
print(list(set(a) & set(b)))


# 19.Create a code to find the union of two lists without duplicates.
a = [1, 2, 3]
b = [2, 3, 4]
print(list(set(a + b)))


# 20.Write a code to shuffle a given list randomly without using any built-in shuffle functions.
import random
lst = [1, 2, 3, 4, 5]
for i in range(len(lst)-1, 0, -1):
    j = random.randint(0, i)
    lst[i], lst[j] = lst[j], lst[i]
print(lst)


# 21.Write a code that takes two tuples as input and returns a new tuple containing elements that are common to both input tuples.
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
result = tuple(set(t1) & set(t2))
print(result)


# 22.Create a code that prompts the user to enter two sets of integers separated by commas.Then ,print the intersection of these two sets.
a = set(map(int, input("Enter first set (comma separated): ").split(',')))
b = set(map(int, input("Enter second set (comma separated): ").split(',')))
print("Intersection:", a & b)


# 23.Write a code to concatenate two tuples.The function should take two tuples as input and return a new tuple containing elements from both input tuples.
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)


# 24.Developma code that prompts the user to input two sets of strings.Then,print the elements that are present in the first set but not in the second set.
a = set(input("Enter first set of strings: ").split())
b = set(input("Enter second set of strings: ").split())
print("Only in first set:", a - b)


# 25.Create a code that takes a tuple and two integers as input.The function should return a new tuple containing elements from the original tuple within the specified range of indices .
def slice_tuple(t, start, end):
    return t[start:end]

t = (10, 20, 30, 40, 50)
print(slice_tuple(t, 1, 4))  # Output: (20, 30, 40)


# 26.Write a code that prompts the user to input two sets of characters.Then,print the union of these two sets.
a = set(input("Enter first set of characters: "))
b = set(input("Enter second set of characters: "))
print("Union:", a | b)


# 27.Develop a code that takes a tuple of integers as input.The function should return the maximum and minimum values from the tuple using tuple unpacking.
def find_max_min(*nums):
    return max(nums), min(nums)

t = (5, 2, 9, 1)
print(find_max_min(*t))


# 28.Create a code that defines two sets of integers.Then,print the union,intersection,and diffeence of these two sets.
a = {1, 2, 3}
b = {2, 3, 4}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a-b):", a - b)


# 29.Write a code that takes a tuple and an element as input .The function should return the count of occurrences of the given element inthe tuple.
def count_element(t, x):
    return t.count(x)

t = (1, 2, 2, 3, 2)
print(count_element(t, 2))  # Output: 3


# 30.Develop a code that prompts the user to input two sets of strings.Then ,print the symmetric difference of these two sets.
a = set(input("Enter first set of strings: ").split())
b = set(input("Enter second set of strings: ").split())
print("Symmetric Difference:", a ^ b)


# 31.Write a code that takes a list of words as input and returns a dictionary where the keys are unique words and the values are the frequencies of those words in the input list.
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)


# 32.Write a code that takes two dictionaries as input and merges them into a single dictionary .If there are common keys,the values should be added together.
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

merged = d1.copy()
for key, value in d2.items():
    merged[key] = merged.get(key, 0) + value

print(merged)


# 33.Write a code to access a value in a nasted dictionary .The function should take the dictionary and a list of keys as input and return the corresponding value .If any of the keys 
# as input and return the corresponding value.If any of the keys do not exits in the dictionary ,the function should return None.

def get_nested_value(d, keys):
    for key in keys:
        if key in d:
            d = d[key]
        else:
            return None
    return d

data = {'a': {'b': {'c': 5}}}
print(get_nested_value(data, ['a', 'b', 'c']))  # Output: 5


# 34.Write a code that takes a dictionary as input and returns a sorted version of it based  on the value .You can choose whethern to sort in ascending or descending  order.
def sort_dict(d, ascending=True):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=not ascending))

data = {"a": 3, "b": 1, "c": 2}
print(sort_dict(data))           # Ascending
print(sort_dict(data, False))    # Descending


# 35.Write a code that inverts a dictionary,swapping keys and values.Ensure that the inverted dictionary correctly handle cases where multiple keys have the same value by storing the 
# keys as a list in the inverted dictionary
def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    return inverted

data = {"a": 1, "b": 2, "c": 1}
print(invert_dict(data))

