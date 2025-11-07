'''a=int(input("enter a number:"))
if(a%2==0):
    print("even")
else:
    print("odd")'''
   
name=input(" name:")
age=int(input("age:"))
if(age>18):
    print("eligible")
    eng=int(input("mark 1:"))
    sci=int(input("mark 2:"))
    math=int(input("mark 3:"))
    eco=int(input("mark 4:"))
    geo=int(input("mark 5:"))
if(eng>25 and sci>25 and math>25 and eco>25 and geo>25):
       a= eng+sci+math+eco+geo
       b= (eng+sci+math+eco+geo)/5
       print("total=",a)
       print("average=",b)
       if(90<b<100):
           print("eligible for enginnering")
       elif(80<b<90):
           print("eligible for atrs")
       elif(70<b<80):
           print("eligible for civil")
       elif(60<b<70):
           print("eligible for mbbs")
       elif(30<b<60):
           print("eligible for bds")

       else:
           print("no elligible courses")

else:
    print("not eligible")
    



        
