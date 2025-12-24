def functionA(name):
   
   def functionB():
      print (name)
   return functionB
   
myfunction = functionA("My name")
myfunction()

def outer_function(x):
    y = 10
    
    def inner_function(z):
        return x + y + z  
    
    return inner_function

closure = outer_function(5)
result = closure(3)
print(result)   
