'''
______
PART 2
______
In the code below, the user is asked to enter three numbers, and then prints a single statement depending on how many of the input numbers are equal. However, there are (at least) 6 syntax errors in the code that need to be fixed. Even after all the syntax errors are fixed and the code runs without errors, there is still a bug. Fix the code so that it runs the way it should.

(Hint: If you see a red squiggly line in the code, that probably means there is a syntax error there.)
'''

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("Enter another number: "))

if(x == y == z):
  print("All three numbers are equal.")

elif(x == y or y == z or x == z):
  print("Exactly two of the numbers are equal.")

else:
  print("None of the numbers are equal.")
