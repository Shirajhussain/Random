# # Write a python program to print "Hello Python"
#
#  print("Hello Python")
#
# # # write a python program to do arithmetical operations  addition and division
#
# # write the code to add two number ??
# A = float(input("Enter the value of A:"))
# B = float(input("Enter the value of B:"))
#
# Ans = A+B
#
# print("Answer is :",Ans)
#
# # write the code to divide two number??
# A = float(input("Enter the value of A:"))
# B = float(input("Enter the value of B:"))
#
# Ans = A/B
#
# print("Answer is :",Ans)
#
# # Find the area of triangle??
# A = float(input("Enter the value of A:"))
# B = float(input("Enter the value of B:"))
#
# Ans = (A*B)/2
#
# print("Answer is :",Ans)
#
# # Swapping the two number ??
# A = float(input("Enter the value of A:"))
# B = float(input("Enter the value of B:"))
#
# temp = A
# A = B
# B = temp
#
# print("After Swapping")
# print("A=",A)
# print("B=",B)
#
#
# # To print Hello 10 times ??
#
# for i in range(10):
#     print("Hello")
#
# # To display  numbers from 0 to 10??
#
# for i in range(11):
#     print(i)
#
# # To display odd numbers from 0 to 20??
#
# for i in range(1, 20, 2):
#     print(i)
#
# # To display numbers from 10 to 1 in descending order??
# for i in range(10, 0, -1):
#     print(i)


#
# n = int(input("Enter a positive integer: "))
#
# total = 0
# i = 1
#
# while i <= n:
#     total = i + total
#     i += 1
#
# print("Sum of first", n, "numbers is:", total)


n = int(input("Enter a digit from 0 to 10: "))

if n == 0:
    print("ZERO")
elif n == 1:
    print("ONE")
elif n == 2:
    print("TWO")
elif n == 3:
    print("THREE")
elif n == 4:
    print("FOUR")
elif n == 5:
    print("FIVE")
elif n == 6:
    print("SIX")
elif n == 7:
    print("SEVEN")
elif n == 8:
    print("EIGHT")
elif n == 9:
    print("NINE")
elif n == 10:
    print("TEN")
else:
    print("PLEASE ENTER A DIGIT FROM 0 TO 10")
