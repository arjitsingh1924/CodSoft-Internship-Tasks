# Simple Calculator
class SimpleCalculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a+self.b
    def substraction(self):
        return self.a -self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        if(self.b != 0):
            return self.a / self.b
        else:
            raise ZeroDivisionError(f" b can not be zero")
a = int(input("Enter the first number: "))    
b =int(input("Enter second number: "))
print("choose operations you want to perform:")
opr = input("Enter one operation symbol out of [ + - * / ]: ")
calcultor = SimpleCalculator(a,b)
def results(calculator,opr):
    if opr == '+':
        print("Addition of a and b = ",calcultor.addition())
    elif opr == '-':
        print("Substraction of b from a = ",calcultor.substraction())
    elif opr == '*':
        print("Multiplication of a and b = ",calcultor.multiplication()) 
    elif opr == '/':
        print("Dvision of a by b  = ",calcultor.division()) 
    else:
        print("Not in operations !")
results(calcultor,opr)        
        
    
    
    
    
