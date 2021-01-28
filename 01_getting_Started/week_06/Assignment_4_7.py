#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85. 

score = input("Enter Score: ")
try: 
    grade=float(score)
except:
        print('Error, please enter a numeric input')
        quit()
def computegrade(grade):
    if grade<0.6:
     return print ('F') 
    elif grade<0.7:   
     return print ('D') 
    elif grade<0.8:   
     return print ('C')   
    elif grade<0.9:   
     return print ('B') 
    elif grade<=1:   
     return print ('A') 
    else:
     return print('invalid input')

p=computegrade(grade)
