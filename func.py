# def number():
   

#     try:
#         n = int(input("Enter Number : "))
#         service = input("Please enter a service : ")

#         if service == "table":
#             for i in range(1,11):
#                 print(i * n)
        
#         elif service == "square":
#             return n ** 2
        
#         elif service == "cube":
#             return n ** 3
        
#         elif service == "power":
#             pow = int(input("Enter Power : "))
#             for _ in range(1,pow):
#                 return n ** pow
#         else:
#             print("Sorry this service is not available.")

#     except Exception as e:
#         print(e)

# print(number())



# def Thala():
#     name = input("Enter Your Name : ").title()

#     if len(name) == 7:
#         print("Thala for a reason.")

#     else:
#         print(f"🖕{name},🖕 Bhad me jaa tu.")

# Thala()



# def nums(*args):
#     s = set()
#     for i in args:
#         if i in s:
#             return True
#         else:
#             s.add(i)
#     return False

# print(nums(1,2,3,4,5,))



# def name():
#     return "Preetam", "Kamble", "pritamkamble343@gmail.com"


# a,b,c = name()
# print(a)
# print(c)


# l = [1,2,4,6,8]

# for i in range(len(l)):
#     print(i , l[i])



# def test8(l):
#     sum = 0
#     for i in l:
#         sum += i

#     return sum
    
# print(test8([1,3,5,4,3,6,5]))



# def test10(a : str , b : int , c : str) -> tuple:
#     """ it will return a tuple with int and strings init."""
#     return a, b , c


# a = test10("Preetam" , 26 , "Kamble")
# print(a)

# print(test10("Kamble" , 9623527612 , "pritamkamble343@gmail.com"))



# def test():
#     return "This is just my test function."

# print(test())



# def test(a,b):  # a,b are positional arguments.
#     return a,b

# print(test(1,4))



# def name(n="Preetam" , k="Kamble"):
#     return k,n

# print(name("preetam" ))




# Use of *args and **kwargs.

# def test(*fuck , a='sorry'):
#     return a , fuck

# print(test(2,44,55,76,[22,33,44],(77,55,44),1234567))



# def dictt(**kwargs):
#     return kwargs

# print(dictt(a = 20 , b = 30 , c = 40))



# def test():
#     def test1():
#         return "This is my  return of test1() function."
#     return test1()

# print(test())



# def outer_func(text):
#     def inner_func():
#         return text.upper()
#     return inner_func()

# print(outer_func("hey guys.."))



# def multiply(m):
#     def multiplayer(n):
#         return n * m
#     return multiplayer

# x = (multiply(5))(6)
# # print(x(12))
# print(x)


# def set_age(age):
#     def validate():
#         if age >= 0 and age <= 60:
#             return True
#         else:
#             return False
#     return 'valid age' if validate() else "Invalid age."


# print(set_age(61))


# def create_print(prefix):
#     def printer(message):
#         return f"{prefix} : {message}"
#     return printer

# x = (create_print("Warning")("your system is going to crash."))
# print(x)



# def calculator():
    
#     a = int(input("Enter value of a : "))
#     b = int(input("Enter value of b : "))
#     operation = input("What you want to do : ")

#     if operation == "add" or operation == "+":
#         return "addition : ", a + b
    
#     if operation == "sub" or operation == "-":
#         return "subtraction : ", a-b
    
#     if operation == 'mult' or operation == "*":
#         return "multiplication : ", a * b
    
#     if operation == 'div' or operation == "/":
#         return "division : ", a / b

# print(calculator())



# def fact_cal():
    
#     def factorial(n):
#         a = 1
#         for i in range(1,n+1):
#             a *= i
#         return a
#     return factorial

# x = fact_cal()
# print(x(5))


# def fact_cal(n):
#     def factorial():
#         a = 1
#         for i in range(1,n+1):
#             a *= i

#         return a
#     return factorial()


# x  = fact_cal(5)
# print(x)


# def fact(n):
#     sum = 1

#     for i in range(1,n+1):
#         sum *= i
#     print(sum)


# fact(5)


# def str_manu(s):
#     def reverse():
#         rev = s[::-1]
#         return rev
    
#     def is_palindrome():
#         rev = s[::-1]
#         if rev == s:
#             return True
#         else:
#             False
    
#     def uppercase():
#         upper = s.upper()
#         return upper
#     return uppercase(), reverse() , is_palindrome()

# x = str_manu("oyo")
# print(x)



# def calculator(a,b):

#     def add():
#         return "Addition : ", a + b
    
#     def sub():
#         return "Subtraction : ", a -b
    
#     def mult():
#         return "Multiplication : ", a * b
    
#     def div():
#         return "Division : ", a / b
    
#     return add(), sub(), mult(), div()

# x = calculator(7,4)
# print(x)




# def IELTS():
#     l = float(input("Enter listening score : "))
#     r = float(input("Enter reading score : "))
#     w = float(input("Enter writing score : "))
#     s = float(input("Enter speaking score : "))

#     if any(score < 0 or score > 9 for score in [l,r,w,s]):
#         return "Error : score should be within 0-9."

#     avg_score = (l + r + w + s) / 4

#     if avg_score - int(avg_score) == 0.1250:
#          band_score == int(avg_score)
    
#     elif avg_score - int(avg_score) >= 0.750:
#          band_score = int(avg_score) + 1

#     elif avg_score - int(avg_score) >= 0.250 and  avg_score - int(avg_score) < 0.750:
#          band_score = int(avg_score) + 0.5

#     else:
#          band_score = round(avg_score / 2) * 2

#     return band_score 

# x = IELTS()
# print(x)




# Find GCD
# Write a function gcd(a, b) that takes two positive integers and returns their greatest common divisor (GCD)

# def gcd(a,b):
    
#     if 1 < a > 100 and 1 < b > 100:
#         return "Error : Enter value within 0 to 100"
    
#     for g in range(100,0,-1):
#         if a // g == 0:      
#             return g
#         break
#     for h in range(100,0,-1):
#         if b // h == 0:
#             return h
#         break
    
#     if g == h:
#         return g


# x = gcd(22,44)
# print(x)



# def calculator():   
#     while True:
#         try:
#             a = int(input("Enter a value of A : "))
#             b = int(input("ENter a value of B : "))
#             operation = input("Enter operation u want : ")

#             if operation == "add" or operation == '+':
#                 print(a + b)
            
#             elif operation == "sub" or operation == '-':
#                 print( a - b)

#             elif operation == "mult" or operation == '*':
#                 print(a * b)
            
#             elif operation == "div" or operation == '/':
#                 print(float(a / b))
#                 # raise Exception ("Zero division Error")
            
#             print("Do you want to calculate more ? ")
#             ans = input("yes or no : ")

#             if ans != "yes":
#                 break
            
                
#         except Exception as e:
#             print("Please enter valid number.")

# calculator()


# def calculator():
#     while True:
#         try:
#             a = float(input("Enter a value for A: "))
#             b = float(input("Enter a value for B: "))
#             operation = input("Enter the operation you want (add, sub, mult, div) or (+, -, *, /): ").strip().lower()

#             if operation in ["add", "+"]:
#                 print(f"The result of {a} + {b} is {a + b}")
#             elif operation in ["sub", "-"]:
#                 print(f"The result of {a} - {b} is {a - b}")
#             elif operation in ["mult", "*"]:
#                 print(f"The result of {a} * {b} is {a * b}")
#             elif operation in ["div", "/"]:
#                 if b != 0:
#                     print(f"The result of {a} / {b} is {a / b}")
#                 else:
#                     print("Error: Division by zero is not allowed.")
#             else:
#                 print("Invalid operation. Please choose add, sub, mult, or div (or +, -, *, /).")
#                 continue

#             ans = input("Do you want to calculate more? (yes or no): ").strip().lower()
#             if ans != "yes":
#                 break

#         except ValueError:
#             print("Please enter valid numbers.")

#     print("Thank you for using the calculator!")

# calculator()



# def dollars_to_inr():
#     dollars = int(input("Enter the total amount in dollasrs : "))

#     inr = 83.77 * dollars

#     return f"Total amount in INR is {inr} "


# print(dollars_to_inr())


# def odd_even():

#     while True:
#         try:
#             num = int(input("ENter a number : "))

#             if type(num) != int:
#                 continue

#             if num % 2 == 0:
#                 return f"Even number: {num}"
#             else:
#                 return f"Odd number : {num}"
            
           
            
#         except Exception as e :
#             print(e)

# print(odd_even())



# def avg(a,b,c):
#     return (a + b + c) / 3


# x = avg(30,50,40)
# print(x)
     


# def count(l):
#     count = 0
#     for name in l:
#         count += 1

#     return count 

# a = count([2,3,4,5,55,44,55,6])
# print(a)



# cities = ["delhi", "mumbai", "pune", "noida", "banglore"]

# def prrint(l):
#     for item in l:
#         print(item.title(), end = ", ")

# prrint(cities)



# def output(func):
#     def wrapper(*c):
#         func(*c)
#         print("Practice and practice...")
#     return wrapper

# @output
# def sqr(n):
#     print( n **2)

# sqr(4)


