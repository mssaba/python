'''print(''register now?:
               1.STUDENT
               2.STAFF
               3.ADDMISSION'')
student=[]
staff=[]
addmission=[]
admin=['admin','admin']

         

def sign(d):
      mail = str(input("enter your mailid:"))
      num= int(input("enter ur mobile number:"))
      us=input("create username:")
      pas=str(input("create new password"))
      if d==1:
           print(' SIGNUP SUCCESSFULL')
           student.append(us)
           student.append(pas)
      elif d==2:
           print( 'SIGNUP SUCCESSFULL')
           staff.append(us)
           staff.append(pas)
      elif d==3:
           print( 'SIGNUP SUCCESSFULL')
           addmission.append(us)
           addmission.append(pas)
d=int(input("select your choice:"))
sign(d)
print(''Student addmission and Managemnt
           
             1. STUDENT
             2. STAFF
             3. ADMISSION
             4. ADMIN'')

    

def select(a):
    if a==4:
        return"admin login"
    elif a==1:
        return 'student login'
    elif a==2:
        return 'staff login'
    elif a==3:
        return 'admission login '
a=int(input('Select your choice:'))
print(select(a))

def login():
    if select(a)=='admin login':
         if b and c in admin:
              return 'valid'
         else:
               return 'invalid'
       
    elif select(a)=='student login':
         if b and c in student:
              return 'valid'
         else:
               return 'invalid'
      
    elif select(a)=='staff login':
         if b and c in staff:
              return 'valid'
         else:
               return 'invalid'
        
    elif select(a)=='addmission login':
         if b and c in addmission:
              return 'valid'
         else:
              return 'invalid'
        
b=str(input("username:"))
c=str(input('password:'))
print(login())'''

sub=['english','math','science']
mark=[43,45,56]
a=dict(zip(sub,mark))
print(a)    
