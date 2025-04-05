# function to add two number
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def avg(num1,num2):
    return num1+num2/2
print("please slect operation:\n" \
      "1.add\n "\
       "2.sub\n "\
        "3.multi\n" \
        "4.div\n" \
        "5.avg\n")
select =int(input("select a operation from 1,2,3,4,5,:"))
number1=int(input("enter first number:"))
number2=int(input("enter a second number:"))
if select == 1:
    print(number1,"+", number2, "=",\
          add(number1,number2))
    
elif select ==2:
      print(number1,"_",number2,"=",\
            sub(number1,number2))
      
elif select ==3:
      print(number1,"*",number2,"=",\
            multi(number1,number2))
      
elif select ==4: 
    print(number1,"/",number2,"=",\
          div(number1,number2))
    
elif select ==5:
    print("(",number1,"+",number2,")", "/","2","=", \
        avg(number1,number2))
else:
    print("invalid operation!plz selct again!")
             
             
             



