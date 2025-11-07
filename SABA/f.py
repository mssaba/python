'''a=10
b=12
a+=b
print(a)

a=str(input("enter a input"))
if(len(a)%2==0):
    b=len(a)//2-1
    c=len(a)//2
    print(a[b:c+1])
else:
    print(a[len(a)//2])'''
name=input(" name:")
age=int(input("age:"))
g=str(input("enter the grp:"))
a="computer science"
b="biology"
if(g==a):
    u=int(input("enter ur chemistry mark:"))
    m=int(input("enter ur math mark:"))
    p=int(input("enter ur physics mark:"))
    c=int(input("enter ur computer mark:"))
    if(u>30 and m>30 and p>30 and c>30):
        r=(u+m+p+c)/4
        print("average",r)
        if(90<r<100):
            choice='''elligilbe for all enineering
                  1.computer engineering
                  2.chemical engineering
                  3.electronics engineering
                  4.mechanical engineerin'''
            print(choice)
            choice=int(input("enter ur choice="))
            if (choice ==1):
                print("YOU HAVE CHOOSEN COMPUTER ENGINEERING ")
                college='''available colleges
                  1.abc enginnering clg
                  2.xyz enhinnering clg
                  3.rst clg of engineering'''
                print(college)
                college=int(input("enter ur college="))
                if (college ==1):
                    print("YOU HAVE CHOOSEN ABc ENGINEERING CLG")
                elif (college == 2):
                    print("YOU HAVE CHOOSEN CHEMICAL ENGINEERING")
                elif(college==3):
                    print("YOU HAVE CHOOSEN ELECTRONICS ENGINEERING")
            

            elif (choice == 2):
                print("YOU HAVE CHOOSEN CHEMICAL ENGINEERING")
                college='''available colleges
                  1.abc enginnering clg
                  2.xyz enhinnering clg
                  3.rst clg of engineering'''
                print(college)
                college=int(input("enter ur college="))
                if (college ==1):
                    print("YOU HAVE CHOOSEN ABC ENGINEERING CLG")
                elif (college == 2):
                    print("YOU HAVE CHOOSEN XYZ ENGINEERING")
                elif(college==3):
                    print("YOU HAVE CHOOSEN RST CLF  ENGINEERING")
            elif(choice==3):
                    print("YOU HAVE CHOOSEN ELECTRONICS ENGINEERING")
                    college='''available colleges
                  1.abc enginnering clg
                  2.xyz enhinnering clg
                  3.rst clg of engineering'''
                    print(college)
                    college=int(input("enter ur college="))
                    if (college ==1):
                        print("YOU HAVE CHOOSEN ABc ENGINEERING CLG")
                    elif (college == 2):
                        print("YOU HAVE CHOOSEN XYZ ENGINEERING")
                    elif(college==3):
                        print("YOU HAVE CHOOSEN RST CLG OF ENGINEERING")
            elif(choice==4):
                print("YOU HAVE CHOOSEN MECHANICAL ENGINEERING")
                college='''available colleges
                  1.abc enginnering clg
                  2.xyz enhinnering clg
                  3.rst clg of engineering'''
                print(college)
                college=int(input("enter ur college="))
                if (college ==1):
                    print("YOU HAVE CHOOSEN ABc ENGINEERING CLG")
                elif (college == 2):
                    print("YOU HAVE CHOOSEN CHEMICAL ENGINEERING")
                elif(college==3):
                    print("YOU HAVE CHOOSEN ELECTRONICS ENGINEERING")

        elif(80<r<90):
            print("elligilbe for chemical enineering")
            print("you have been selceted in qwr clg")
        elif(70<r<80):
            print("elligilbe for electronics enineering")
            print("you have been selected for bbq clg")
        elif(60<r<70):
            print("elligilbe for mechanical enineering")
            print("no clg for u go to hell")


            
elif(g==b):
    t=int(input("enter ur chemistry mark:"))
    q=int(input("enter ur biology mark:"))
    x=int(input("enter ur physics mark:"))
    y=int(input("enter ur maths mark:"))
    if(t>30 and q>30 and x>30 and y>30):
        w=(t+q+x+y)/4
        print("average",w)
        if(90<w<100):
            choice='''elligilbe for all course
                  1.MBBS
                  2.BDS
                  3.BPT
                  4.PSYCHOLOGY'''
            print(choice)
            choice=int(input("enter ur choice="))
            if (choice ==1):
                print("YOU HAVE CHOOSEN MBBS")
                college='''available colleges
                  1.abc medical clg
                  2.xyz medical  clg
                  3.rst clg of medicine'''
                print(college)
                college=int(input("enter ur college="))
                if (college ==1):
                    print("YOU HAVE CHOOSEN ABc medical CLG")
                elif (college == 2):
                    print("YOU HAVE CHOOSEN xyz medical  clg")
                elif(college==3):
                    print("YOU HAVE CHOOSEN rst clg of medicine")
            elif (choice == 2):
                print("YOU HAVE CHOOSEN BDS")
                college='''available colleges
                  1.abc medical clg
                  2.xyz medical  clg
                  3.rst clg of medicine'''
                print(college)
                college=int(input("enter ur college="))
                if (college ==1):
                    print("YOU HAVE CHOOSEN ABc medical CLG")
                elif (college == 2):
                    print("YOU HAVE CHOOSEN xyz medical  clg")
                elif(college==3):
                    print("YOU HAVE CHOOSEN rst clg of medicine")
            elif(choice==3):
                print("YOU HAVE CHOOSEN BPT")
                college='''available colleges
                  1.abc medical clg
                  2.xyz medical  clg
                  3.rst clg of medicine'''
                print(college)
                college=int(input("enter ur college="))
                if (college ==1):
                    print("YOU HAVE CHOOSEN ABc medical CLG")
                elif (college == 2):
                    print("YOU HAVE CHOOSEN xyz medical  clg")
                elif(college==3):
                    print("YOU HAVE CHOOSEN rst clg of medicine")
            elif(choice==4):
                print("YOU HAVE CHOOSEN PSYCHOLOGY ")
                college='''available colleges
                  1.abc medical clg
                  2.xyz medical  clg
                  3.rst clg of medicine'''
                print(college)
                college=int(input("enter ur college="))
                if (college ==1):
                    print("YOU HAVE CHOOSEN ABc medical CLG")
                elif (college == 2):
                    print("YOU HAVE CHOOSEN xyz medical  clg")
                elif(college==3):
                    print("YOU HAVE CHOOSEN rst clg of medicine")
            
        elif(80<w<90):
            print("elligilbe for BDS")
            print("selected in ams medical clg")
        elif(70<w<80):
            print("elligilbe for BPT")
            print("selected in fsdg clg ")
        elif(60<w<70):
            print("elligilbe for PSYCHOLOGY")
            print("no medical clg available")

        

    





