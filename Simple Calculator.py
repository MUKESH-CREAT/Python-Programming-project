def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divided(a,b):
    return a/b
def avg(a,b):
    return (a+b)/2


print("Pls select an operation \n" "1.addition \n" "2.Substraction \n" "3.multiplication \n"\
      "4.division \n" "5.average \n")
Select =int(input("select an operation from 1,2,3,4,5 : "))
number1 = int(input("enter first no. : "))
number2 = int(input("enter second no. : "))
if Select ==1:
    print(number1,"+",number2 ,"=",add(number1,number2))

elif Select ==2:
    print(number1,"-",number2,"=",sub(number1,number2))6
elif Select==3:
    print(number1,"*",number2,"=",multiply(number1,number2))
elif Select == 4:
    print(number1,"/",number2,"=",divided(number1,number2))
elif Select ==5:
    print("average of",number1,"and",number2,"is",avg(number1,number2))
else :
  print("Invalid operation! Please select again ")
    
          

