#Error
#There are some types of error which are raised during the compilation of the prgram
#exception handiling (these error are caused by invalid inputs or missing files)
#assert statement (it causes in if else conditon )
#try-except block(it helps to run the progam without any break even if there is a error)
#example
try:
   number = int(input("Enter a number: "))
   result = 10 / number
   print(f"Result: {result}")
except ZeroDivisionError as e:
   print("Cannot divide by zero.")
#try-finally block
try:
    n = int(input('enter a number:'))
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")
#raise
def divide(a, b):
    if b == 0:
      raise ValueError("Cannot divide by zero")
      return a / b

try:
   result = divide(10, 0)
except ValueError as e:
   print(e)


