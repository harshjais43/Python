# # creating a funtion

# def onefunction():
#     print("Hello")

# # calling a funtion 

# onefunction()

# # argument

# def twofunction(fname):
#     print(fname +" Refsnes")

# twofunction("harsh")
# twofunction("one")
# twofunction("rahul")

# def threefunction(fname,lname):
#    print(fname + " " + lname)
# threefunction("harsh" , "jaiswal") 

# arbitrary arguments 

# def myfunction(*kids):
#     print("The kids are " , kids[3])

# myfunction("Emil", "Sophia", "Jaden", "Mila")  # output: The kids are

# def my_function(child1, child2 , child3):
#     print("The children are " , child3)

# my_function(child1 = "emil" , child2 = "harsh" ,child3  ="one")

# def my_function(country = "Norway"):
#     print("I am from " , country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(x):
#     return x * 5 

# print(my_function(3))
# print(my_function(5))
# print(my_function(6))

# def my_function(x,/):
#     print(x)

# my_function(3) 

# def my_function(x):
#     print(x)

# my_function(x = 3)       

# def my_function(* , x ):
#     print(x)
# my_function(x=3)


# def my_function(a , b , / , * , c , d):
#     print(a+b+c+d)


# def add(num1: int , num2 : int) -> int:
#     """ add two numbers"""
#     num3 = num1 + num2
     
#     return num3 

# num1, num2 = 5 , 7
# ans = add(num1 , num2)
# print(f"the addition of {num1} and {num2} is {ans}") # output: the addition of 5 and 7

# key word argument 

# def student(firstname , lastname):
#     print(firstname, lastname)

# student(firstaname = 'Geeks' , lastname = 'Pratice') 
# student(lastname = 'Pratice', firstname = 'Geeks')   

# Variable length keyword arguments
# def myfub(**kwrgs):
#     for key, value in kwrgs.items():
#         print("%s == %s" % (key, value))

# myfub(first='Geeks', mid = 'for' , last='Geeks')

# def f1():
#     s = 'i love me'

#     def f2():
#         print(s)

#     f2()

# f1()

# def cube(x): return x*x*x

# cube_v2 = lambda x : x*x*x

# print(cube(7))
# print(cube_v2(7)) 

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(4))   

# v = "nipun " 
# a = v.replace('n','t')

# print(a)

