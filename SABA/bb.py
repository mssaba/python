#string operation

s= " welcome to mayiladuthurai "

#length
print(len(s))
print(len(s)//2)#middle value
print(s[len(s)//2])#middle letter
print(len(s)-1)#index value


#upper,lower case
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())

#removing function

print(s.strip())
print(s.rstrip())
print(s.lstrip())

#checking function

print(s.startswith(" wel"))
print(s.endswith(" "))
print(s.isalpha())
print(s.isalnum())
print(s.isdigit())
print(s.islower())
print(s.isupper())

#index

print(s.find("w"))
print(s.replace("welcome","warm welcome"))
print(s.count("e"))

#split and join

print(s.split("o"),s)
print("=".join(s))

#format

print(f"hi,{s}")
print(f"hi,warm{s}")

#encode decode
print(s.encode())
S=s.encode()
print(S.decode())
print(s[::-1])#reverse

#indexing
print(s[3])
print(s[3:5])
print(s[-5:-2])
print(s[:8])
print(s[5:])
print(s[::2])
print(s[::-2])


a=s.upper()
print(a)

a=str(input("Enter the name="))
b=int(input("enter age="))
print(type(a))
print(type(b))
