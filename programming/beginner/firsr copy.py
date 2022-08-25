# print("hello world")
# x = 4
# x = x + 1 
# print(x)
# print(float(99) + 100)
# sale = 43
# type(sale)
# print(type(sale))
# enp = input("euorope floor")
# usf = int(enp) + 1
# print("US floor" , usf)
# x = 5 
# if x > 2 :
#     print("bigger")
# else :
#      print("smaller")
# print("all done")

# x = 20
# if x < 2 :
#     print("small")
# elif x < 10 :
#     print("medium")
# elif x < 15 :
#     print("big")
# else:
#     print("too big")

# def print_lyrics() :
#     print("hello from the other side")
#     print("i wish there was some light")
# print("yo how it been")
# print_lyrics()

# def greet(lang):
#     if lang == 'es' :
#         print("hola")
#     elif lang == ('fr') :
#         print('bonjour')
#     else :
#         print('hello')
# greet('es')
# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# # print("Done!")
# for i  in [5, 4, 3, 2, 1] :
#     print(i)
# print("blastoff")
# friends = ['majdi', 'bilal', 'jamal']
# for friend in friends :
#     print("happy birthday" , friend)
# from xml.dom.expatbuilder import theDOMImplementation

# LOOPS AND ITERATION: LOOP IDIOMS
# largest_so_far = -1
# print('before', largest_so_far)
# for the_num in [7, 4, 7, 19, 18, 6, 74, -4, 81] :
#     if the_num > largest_so_far :
#         largest_so_far = the_num
#     print(largest_so_far, the_num)
# print('after', largest_so_far)

# LOOPS AND ITERATION: MORE LOOP PATTERNS
# count = 0
# sum = 0
# print('before', count, sum)
# for value in [9, 41, 58, 3, 98, 27, 46] :
#     count = count + 1
#     sum = sum + value
#     print(count, sum ,value)
# print('after', count, sum, sum / count)

# smallest = None
# print('before')
# for value in [3, 6 ,13, 67, 1, 7] :
#     if smallest is None :
#         smallest = value
#     elif value < smallest :
#         smallest = value
#         print('after', smallest)
# print('after', smallest)

# current = 1000000
# for value in [9, 41, 58, 7] :
#     if value < current :
#         current = value
# print(current)

# def average(array):
#     sum = 0
#     for num in array:
#        sum += num
#     mean = sum / len(array)
# fruit = 'banana'
# print(len(fruit)
# fruit = 'apple'
# index = 0
# while index < len(fruit) :
#    letter = fruit[index]
#    print(index, letter)
#    index = index + 1
# fruit = 'banana'
# for letter in fruit :
#    print(letter) 

# x= 2
# y= 3
# if x == 2:
#    if y == 3:
#       print('x = 2, y = 3')
#    else:
#       print('x = 2, y != 3')
# else:
#    print('x != 2')      

# for x in range(0, 10, 5):
#    p

# loop = True
# while loop:
#    name = input('insert something: ')
#    if name == 'stop':
#       loop = False
#       break

# fruits = ['apple', 'peach', 'banana', 'orange', 3, 8, 90]
# for fruit in fruits:
#    if fruit == 'peach':
#       print(fruit)
#    else:
#       print('not peach')
      
# (len(fruits))
 
# text = input('input something: ')
# print(len(text))

# wife = input('input something: ')
# print(wife.split('hi'))

# people = ['majdi', 'bilal', 'farid', 'ihab']
# text = 'Hello i like python'
# people[2:2] = 'karim'
# print(people)


# def addTwo(x):
#    return (x + 2)**2

# def subTwo(y):
#    return y - 2
# NewNumber = addTwo(7)
# print(NewNumber)

# string = 'hellotglmhfjbgjhegbrilubhflkjsa;guiha;eriu'
# print(string.count('h'))
# string = input('please type something: ')
# if string.count('_') > 0:
#    print('Not good!')
# else:
#    print('Good!')
# password = "karim"
# tries = 5
# while tries != 0:
#     inp = input("Enter pass: ")
#     if(inp == password):
#         print("Success!")
#         break
      
#     elif (tries == 0):
#         print("incorrect")
#         break
#     else:
#         tries = tries - 1
#         print('Try again')
#         continue

#     input("Enter pass: ")
#     if tries == 0:
#         print('no tries available')
#         break 
# import math
# print(math.pi)
# # import MyModule
# def func(x, text):
#    print(x)
#    if text == '1':
#       print('text is one')
#    else:
#       print('text is not one')

# func('tim', '1')   
# text = input('username: ') 
# try:
#    number = int(text)
#    print(number)
# except:
#    print('invalid username')

# var = 9
# loop = True
# # newVar = 34
# def func(x):
#    newVar = 7
#    if x == 5 :
#       return newVar
# print(newVar)

# def otherFunc():
#    newVar = 5
#    print(newVar)
# otherFunc()

from re import X


x = 'string'
y = 23
boo = True

class number():
   def __init__(self, num) :
      self.var = num

   def display(self, x):
      print(x)

num = number(23)
print(num)
num.display(num.var)
print(x.count(1))
