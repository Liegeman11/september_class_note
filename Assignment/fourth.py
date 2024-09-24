# read on different strings method and application

# solution

# 1. capitalize()
# Application: Converts the first character of the string to uppercase and the rest to lowercase.
# message = "good morning"
# print(message.capitalize())

# 2. lower()
# Application: Converts all characters in the string to lowercase.
# name = "TAIWO"
# print(name.lower()) 

# 3. upper()
# Application: Converts all characters in the string to uppercase.
# name = "taiwo"
# print(name.upper()) 

# 4. title()
# Application: Converts the first character of each word to uppercase.
# message = "good morning"
# print(message.title())  

# 5. swapcase()
# Application: Swaps uppercase characters to lowercase and vice versa.
#  message = "Good Morning"
#  print(message.title()) 

# 6. strip()
# Application: Removes leading and trailing whitespace (or characters) from the string.
name = "  taiwo  "
print(name.strip()) 

# lstrip(): Removes leading characters.
print(name.lstrip())

# rstrip(): Removes trailing characters.
print(name.rstrip())  


# 7. replace(old, new)
# Application: Replaces occurrences of the substring old with new.
message = "good morning"
print(message.replace("morning", "Python"))


# 8. find(substring)
# Application: Returns the index of the first occurrence of substring. Returns -1 if not found.
message = "good morning"
print(message.find("morning")) 

# rfind(): Finds the last occurrence of substring.
print(name.rfind("o")) 

# 9. count(substring)
# Application: Returns the number of non-overlapping occurrences of substring.
fruit = "banana"
print(fruit.count("a")) 

# 10. split(separator)
# Application: Splits the string into a list of substrings based on the given separator. If no separator is specified, it splits on whitespace.

fruit = "apple,banana,orange"
print(fruit.split(",")) 

# rsplit(separator): Splits from the right.
print(fruit.rsplit(",", 1)) 

# 11. join(iterable)
# Application: Joins elements of an iterable (e.g., list) into a single string with a specified separator.
fruits = ['apple', 'banana', 'orange']
fruit = ", ".join(fruits)
print(fruit)  # "apple, banana, orange"






