# Password generator
# n = length of password 
import random
allsymbols = "!@$%&*-+$?"
allcharsanddigits = "abcdefghijklmnopqrstuvwxyz123456789"
n = int(input("enter length of pasword: "))
def passwordGenerator(n):
    password =""
    for i in range(n):
        if(i % 3 == 1):
           password += random.choice(allsymbols) 
        else:
            password += random.choice(allcharsanddigits)
    return password        
print(passwordGenerator(n))            
    
