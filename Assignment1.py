#1 Simple function which prints “Name”
def print_name():
    print("Piyush")

print_name()




#2 Function which expects two arguments and prints them
def print_two(a, b):
    print(a)
    print(b)

print_two(10, 20)




#3 Function which expects an unknown number of arguments
def print_args(*args):
    for i in args:
        print(i)

print_args(1, 2, 3, 4, 5)





#4 Function which expects keyword arguments (kwargs)
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_kwargs(name="Piyush", age=21, course="Python")





#5 Function which expects a list as an argument
def print_list(lst):
    for item in lst:
        print(item)

print_list([10, 20, 30, 40])





#6 Function to find the maximum of four numbers
def max_of_four(a, b, c, d):
    return max(a, b, c, d)

print(max_of_four(10, 25, 5, 15))





#7 Function to sum all numbers in a list
def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total

print(sum_list([1, 2, 3, 4, 5]))






#8 Function to multiply all numbers in a list
def multiply_list(lst):
    result = 1
    for i in lst:
        result *= i
    return result

print(multiply_list([1, 2, 3, 4]))






#9 Function to check whether a number falls in a given range
def check_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False

print(check_range(10, 5, 15))






#10 Function to check whether a number is even or odd
def even_or_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd(7)



#11 
def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# Example
print(unique_list([1, 2, 2, 3, 4, 4, 5]))





#12
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Example
num = 7
if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")




#13
def print_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            print(num, end=" ")

# Sample List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even_numbers(numbers)





#14
def is_palindrome(s):
    return s == s[::-1]

# Example
word = "madam"
if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")





#15
def find_min(a, b, c):
    return min(a, b, c)

# Example
print(find_min(10, 5, 8))



#21
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26

    for ch in s:
        count[ord(ch) - ord('a')] += 1

    for ch in t:
        count[ord(ch) - ord('a')] -= 1

    for c in count:
        if c != 0:
            return False

    return True
