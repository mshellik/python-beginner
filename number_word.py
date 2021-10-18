'''
num=eval(input("Enter your number :"))
if num==1:
    print("One")
elif num==2:
    print("Two")
elif num==3:
    print("Three")
elif num==4:
    print("Four")
elif num==5:
    print("Five")
elif num==6:
    print("Six")
elif num==7:
    print("Seven")
elif num==8:
    print("Eight")
elif num==9:
    print("Nine")
elif num==10:
    print("Ten")
else:
    print("You should be entering the range betwwen 1-10")
'''
'''
num=eval(input("Enter your number : "))

if num in [1,2,3,4,5,6,7,8,9,10]:
    if num==1:
        print('one')
    elif num==2:
        print('two')
    elif num==3:
        print('three')
    elif num==4:
        print('four')
    elif num==5:
        print('five')
    elif num==6:
        print('six')
    elif num==7:
        print('seven')
    elif num==8:
        print('eight')
    elif num==9:
        print('nine')
    elif num==10:
        print('ten')
else: 
    print('Enter the number between 1 -10')
'''

#Using Dictionary 

num=eval(input('Please enter your number : '))

number_dict={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}

if num==number_dict.get(num):
    print(number_dict.value(num))
