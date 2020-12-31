def calc(num1,num2,operator):
    if (operator == "+"):
        return (num1+num2)
        
    elif(operator == "-"):
        return (num1-num2)
    
    elif(operator == "*"):
        return (num1*num2)
    
    elif(operator == "/"):
        if (num2 == 0):
            print("Mathematical error")
        else:
            return (num1/num2)
        
    elif(operator == "%"):
        return (num1%num2)
        
    elif(operator == "s"):
        return (num1**2)
    
    elif(operator == "c"):
        return (num1 ** 3)
        
    else :
        return (num1 ** 0.5)

print("Use calc")
print("Please choose your option")
print(" + for  Add\n - for Sub\n * for Mul\n \ for Div\n % \\for Modulas\n s for Square\n c for cube\n z for sq root" )
operator_list= ['+','-','*','/','%','s','c','z']
operator = input("\nPlease enter operator")
print(type(operator))
while (operator not in operator_list):
    operator =input("please enter correct operator")

num1 = int(input("enter num1"))
if (operator in operator_list[5:]):
    num2 = 0
else: 
    num2 = int(input("enter num2"))
    


result = calc(num1,num2,operator)

print (result)
    