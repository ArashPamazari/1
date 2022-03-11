vazn = float(input('vazne khod ra vared konid: '))

ghad = float(input("ghad khod ra vared konid: "))

Bmi= vazn / ghad 

if Bmi < 18.5 :
    print('underwighted')

if 18.5 < Bmi < 24.9 :
    print('normal')

if 25 < Bmi < 29.9 :
    print('overwighted') 

if 30 < Bmi < 34.9 :
    print('obese')

if 35 < Bmi :
    print('extremly obese')
