###What is inbuilt python function? (Explain with example)
# An inbuilt Python function refers to a function that is provided by the Python language itself as part of its standard library. These functions are readily available for use without requiring any additional installation or imports. Python has a wide range of these inbuilt functions, which help perform common tasks like data type conversions, mathematical operations, handling input/output, and more.
# Examples of Inbuilt Python Functions:

# 1. **print()**: Outputs data to the console.
print("Hello, World!")  # Outputs: Hello, World!
   

# 2. **len()**: Returns the length of an object (like a string, list, or tuple).
my_list = [1, 2, 3, 4]
print(len(my_list))  # Outputs: 4


# 3. **type()**: Returns the type of an object.
x = 10
print(type(x))  # Outputs: <class 'int'>


# 4. **input()**: Reads input from the user as a string.
name = input("Enter your name: ")
print("Hello, " + name + "!")

print('my name is ' +name+ '.')
# 5. **int(), float(), str()**: Convert data to an integer, float, or string, respectively.
num_str = "100"
num_int = int(num_str)
print(num_int)  # Outputs: 100


# 6. **sum()**: Returns the sum of elements in an iterable (like a list or tuple).
numbers = [1, 2, 3, 4]
print(sum(numbers))  # Outputs: 10


# 7. **min() and max()**: Return the minimum and maximum values in an iterable.
numbers = [1, 2, 3, 4]
print(min(numbers))  # Outputs: 1
print(max(numbers))  # Outputs: 4


# 8. **abs()**: Returns te absolute value of a number.
print(abs(-5))  # Outputs: 5


# 9. **round()**: Rounds a floating-point number to a specified number of decimal places.
print(round(3.14159, 2))  # Outputs: 3.14

# 10. **sorted()**: Returns a sorted list from the elements of an iterable.
numbers = [3, 1, 4, 1, 5]
print(sorted(numbers))  # Outputs: [1, 1, 3, 4, 5]

###what is concatenation (Explain with example)
# Concatenation in Python means joining two or more sequences (such as strings, lists, or tuples) together to form a single, combined sequence. This process is done using the + operator.

## Types of Concatenation:

# 1. *String Concatenation*:
#    - In Python, you can concatenate (join) strings using the + operator.
#    - Example:
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Outputs: Hello World


# 2. *List Concatenation*:
#    - You can also concatenate lists using the + operator, which will create a new list containing all the elements from the concatenated lists.
#    - Example:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Outputs: [1, 2, 3, 4, 5, 6]


# 3. *Tuple Concatenation*:
#    - Similar to lists, you can concatenate tuples using the + operator.
#    - Example:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Outputs: (1, 2, 3, 4, 5, 6)

###what variable
# In programming, a variableis a symbolic name or identifier that is used to store data or values in a program. Think of a variable as a container that holds information that can be referenced and manipulated throughout your code.

## Key Concepts of Variables:

# 1. *Naming Variables*:
#    - Variables are given names to identify them. These names must start with a letter or an underscore (_), and they can contain letters, digits, and underscores.
#    - Example:
age = 25
name = "Alice"
is_student = True


# 2. *Assigning Values*:
#    - The = operator is used to assign a value to a variable.
#    - Example:
x = 10  # The variable x now holds the value 10
y = "Hello"  # The variable y holds the string "Hello"


# 3. *Types of Variables*:
#    - Variables can hold different types of data, such as numbers, strings, lists, and more.
#    - Example:
num = 42  # An integer variable
pi = 3.14  # A floating-point variable
greeting = "Hi there!"  # A string variable
numbers = [1, 2, 3]  # A list variable


# 4. *Using Variables*:
#    - Once a variable has been assigned a value, you can use it throughout your program by referencing its name.
#    - Example:
y = 10
x = 5
z = x + y
print(z)  # Outputs: 15


# 5. *Updating Variables*:
#    - The value of a variable can be updated by assigning a new value to it.
#    - Example:
counter = 1
counter = counter + 1  # counter now holds the value 2


# 6. *Variables as References*:
#    - In Python, variables act as references to the values they hold. This means that when you assign a variable to another, both variables point to the same data until one of them is reassigned.
#    - Example:
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # Outputs: [1, 2, 3, 4]
