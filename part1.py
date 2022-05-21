'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''

x = int(input("Enter a number: "))

y = int(input("Enter another number: "))

z = int(input("Enter another number: "))

if x < y and x < z:
  print("The smallest number is ", x)
elif x > y and x > z and y == z:
  print("The smallest number is ", y)
elif x == y == z:
  print("The smallest number is ", x)
elif y < x and y < z:
  print("The smallest number is ", y)
elif y > x and y > z and x == z:
 print("The smallest number is ", x)
elif z < x and z < y:
 print("The smallest number is ", z)
elif z > x and z > y and x == y:
  print("The smallest number is ", x)