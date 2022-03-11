import math

numberOne = int(input('adade aval ra vared konid: '))
numberTwo = int(input('adade Dovom ra vared konid: '))

OP= input('AmalGar morede nazar ra vared konid: ')

if OP=='+':
    result= numberOne + numberTwo

if OP=="-":
    result= numberOne - numberTwo

if OP=='*':
    result= numberOne * numberTwo

if OP=='/':
    if numberTwo != 0:
        result=numberOne/numberTwo
    else:
        print('khata!!!')

if OP=="rad":
    result= math.sqrt(numberOne)

if OP=='sin':
    result= math.sin(numberOne)

if OP=='tan':
    result=math.tan(numberOne)        

if OP == 'cot':
    result= math.tan(1/numberOne)

if OP == 'cos':
    result = math.cos(numberOne)

if OP == 'fac':
    result=math.factorial(numberOne)
    

print(result) 
