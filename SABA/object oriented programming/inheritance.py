#inheritance
#it has a parent and the child class
#types of inheritance
#single in heritance
#multiple inheritance
#multilevel inhareitance
#hierarical inheritance
#hybrid inheritance


#single inheritance
class parent:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def func1(self):
        print(f'{self.fname} {self.lname}')

a=parent('john','doe')
a.func1()

class child(parent):
     def __init__(self, fname, lname):
         super().__init__(fname, lname)

b=child('jane','doe')
b.func1()

#multiple inheritance
class division:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def divide(self):
      return self.n/self.d
   
class modulus:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def mod_divide(self):
      return self.n%self.d
      
class div_mod(division,modulus):#inheritance from two classes
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def div_and_mod(self):
      divval=division.divide(self)
      modval=modulus.mod_divide(self)
      return (divval, modval)
   
x=div_mod(5,5)
print ("division:",x.divide())
print ("mod_division:",x.mod_divide())
print ("divmod:",x.div_and_mod())

#multilevel inheritance
class garndpa:
   def grandpa(self):
      print("i am grandpa")
class father(garndpa):
   def father(self):
      print("i am dad")
class son(father):
   def son(self):
      print("i am son")
p=son()
p.grandpa()
p.father()
p.son()

#hierarchical inheritance
class mother:
   def mother(self,name):
      self.name=name
      print("mother name is:",self.name)
class daughter(mother):
   def daughter(self,name):
      self.name=name
      print("daughter name is:",self.name)
class son(mother):
   def son(self,name):
      self.name=name
      print("son name is:",self.name)
d=daughter()
d.mother("alice")    
d.daughter("lily")
s=son()     
s.mother("alice")
s.son("bob")


#hybrid inheritance
class A:
    def funcA(self):
        print("Function A from class A")
class B(A):
      def funcB(self):
         print("Function B from class B")
class C(A):
      def funcC(self):
         print("Function C from class C")
class D(B,C):  
      def funcD(self):
         print("Function D from class D")
d=D()
d.funcA()   
d.funcB()
d.funcC()
d.funcD()
