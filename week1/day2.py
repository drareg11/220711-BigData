
x = 0
print(x)


while True:
    x += 1
    #if x == 8: 
        #continue
    if x > 12:
        break
    print(x)


#while x <= 12:
   # x += 1
   # if x ==8:
       # continue
   # print(x)
        
#if x < 13:
   # print("X is less THAN 13!")
#elif x == 13:
       # print("X is 13!")
#else:
        #print("X IS GREATER THAN 13!")

#print("The value of x Is", x)



#if x < 13:
        #print("X IS LESS THAN 13!")
#elif x == 13:
        #print("X IS 13!")
#else:
        #print("X IS GREATER THAN 13!")

#print("The value of x is", x)


# from math import prod
# from traceback import print_tb
# import day2_module1 as m1
#def main():
 #   print(mult_2(2, 8))
#     #m1.print_congrats()
#     lst = [0, 1, 2, 3, 4, 5]
#     lst_names = ["a", "s", "fd"]
#     #for i in range(len(lst)):
#     #    print(lst[i])
#     #for elem in lst:
#     #    print(elem)
#     #for elem in lst_names:
#         #if len(elem) == 1:
#             #print(elem)
# if __name__ == "__main__":
#    main()
# #multi line 

# #import day2_module1 as m1

# #def main():
#     #print(m1.mult_2(2, 8))
#     #m1.priint_congratulations()

#     #lst = [0, 1, 2, 3, 4, 5]

#     #for i in range(len(lst)):
#       #  print(lst[i])

#     #for elem in lst:
#         #print("Element: " + str(elem))

#         DAY2_MODULE1
# 3:26
# def mult_2(x, y):
#  print("Entering mult_2 function... multip.", x, " and ", y)
#  return x*y
# def print_congrats():
#     print("WINNER WINNER")

#import day2_module1 as m1

#def main():
    #print(m1.mult_2(2, 8))
    #m1.print_congratulations()

    #lst = [0, 1, 2, 3, 4, 5]

    #count =0
    #while count < 6:
       # print(lst[count])
        #count += 1


    #for i in range(len(lst)): # same as for (int i =0; i < lst.length; i++) as we would in JAVA 
        #print(lst[i])

#def mult_2(x, y): ***** CAN be used but we are utilizing the IMPORT example**********
   # print("Entering mult_2 function ... multiplying", x, "and", y)
    #return x*y


#if __name__ == "__main__":
    #main()







''''
def mult_2(x, y):
    print("Entering mult_2 function ... multiplying", x, "and", y)
    return x*y

prod = mult_2(2, 4)
print(prod)

prod = mult_2(5, 6)
print(prod)

prod = mult_2("Hello", 4)
print(prod)

f = lambda x, y : x * y 
print(f(4, 5))

'''
'''
def funct_2(x, y, f):
    print("Entering funct_2 function...")
    return f(x, y)

f1 = lambda x, y : x * y
f2 = lambda x, y : x - y

print(funct_2(10, 20, f1))
print(funct_2(10, 20, f2))
'''