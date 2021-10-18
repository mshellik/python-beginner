num=eval(input('Please enter your number : '))

number_dict={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}

if num in number_dict.keys():
    print(number_dict.get(num))
else:
    print("You need to enter the number betweek 1 to 10"))
