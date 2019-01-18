#program that gives letter grades

#define variables
grade = float(input('Enter grade: '))

if grade >= 90:
    print('Your letter grade is: A')

elif grade >= 80:
    print ('Your letter grade is: B')

elif grade >= 70:
    print('Your letter grade is: C')

elif grade >= 60:
    print('Your letter grade is: D')

else:
    print('Your letter grade is: F')
        
