# #pets
# pets = {'bird':3.5,'cat':5.0,'dog':7.25,'gerbil':1.5}
# try:
#     pet_name = input("Enter a pet:")
#     float_price= float(pets[pet_name])
#     print("The price of {0} is {1}".format(pet_name,float_price))
# except:
#     print("Invalid pet is picked! Please try again")

#calculator
def calculator(num1,num2,operator):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-'
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator =='/':
            return num1/num2
    except:
        print("Enter valid number")


op=input("Enter the operation you want:1. + 2.- 3. *4. '\'")
number1 = input("Enter the first number")
number1 = float(number1)
number2 = input("Enter the second number")
number2 = float(number2)
result = calculator(number1,number2,op)
print(result)
