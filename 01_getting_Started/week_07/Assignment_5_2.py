# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#  Once 'done' is entered, print out the largest and smallest of the numbers.
#  If the user enters anything other than a valid number catch it with a try/except and
#  put out an appropriate message and ignore the number.
#  Enter 7, 2, bob, 10, and 4 and match the output below. 

num=0
tot=0.0
largest= None
smallest= None
while True:
    sval= input('Enter a number:')
    if sval=='done' :
        break
    try:
       fval= float(sval)
    except:
        print('Invalid input')
        continue
    #print(fval)
    #print(fval)
    num=num+1
    tot=tot+fval
    #maximo
    if largest is None :
        largest=fval
    elif fval>largest :
        largest= fval
    #minimo
    if smallest is None :
        smallest=fval
    elif fval<smallest :
        smallest= fval
#print el proceso ha terminado
#print ('ALL DONE')
#print (tot,num, tot/num)
print ('Maximum is',int(largest))
print ('Minimum is',int(smallest))