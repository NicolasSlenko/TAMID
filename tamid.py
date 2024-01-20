#Note: I know we were only told to do 2, but I wanted to complete the rest for my own practice

#Author: Nicolas Slenko

#Challenge 1: Sorting (took me way too long to think of this lol) (1 line)
def sortArrays(arr1, arr2, k):
  return sorted((arr1 + arr2))[:k]

#Challenge 2: Calculator (More than 15 lines, but since this is a "program" and not a method, I assumed it was ok)
def calculator():
  while(input("Continue? (y/n): ") != "n"):
    try:
      x = float(input("Number 1: "))
      y = float(input("Number 2: "))
    except:
      print("Must be valid numbers")
      continue
    op = input("Operation: ")
    if len(op) != 1 and op not in {'+', '-', '*', '%', '/'}:
      print("Invalid operation")
      continue
    if op == "+":
      print(x+y)
    if op == "-":
      print(x+y)
    if op == "*":
      print(x*y)
    if op == '%' and y != 0:
      print(x%y) 
    elif op == "/" and y != 0:
      print(x/y)
    elif y == 0:
      print("Can't divide by 0 silly!")
  else:
    print("Goodbye")


#Challenge 3: Boxed String (12 lines)
def boxedString(lst):
    width = len(max(lst, key=len)) + 4
    for _ in range(width):
        print('*', end='')
    print('')
    for x in lst:
      if len(x) + 4 == width:
        print('*', x,' ' * (width - len(x) - 6) + '*')
      else:
        print('*', x,' ' * (width - len(x) - 5) + ' *')
    for _ in range(width):
        print('*', end='')

#Challenge 4: Palindrome (1 line)
def isPalindrome(string):
  return string == string[::-1] 
   
