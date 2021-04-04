#Grade Calculator with while loop python_
#PROTOTYPE 2

" Computer Programming Tutor_April 3, 2021"
grade = 0
total =0
for k in range(0,5):
    if grade >= 0 and grade <= 100:
        grade = int(input("What was your Score Subject"+ str(k+1)+ "?:"))
        total +=grade
    elif grade>=101:
        grade = int(input("It should be a number from 0 to 100, What was your Score?:"))
        total +=grade
    grade =total/5

    if 93<= grade <=100:
        print("Your Grade is = A")
    elif 90 <= grade <93:
        print("Your Grade is = A-")
    elif 87 <= grade <90:
        print("Your Grade is = B+")
    elif 83 <= grade <87:
        print("Your Grade is = B")
    elif 80 <= grade <83:
        print("Your Grade is = B-")
    elif 77 <= grade <80:
        print("Your Grade is = C+")
    elif 73 <= grade <77:
        print("Your Grade is = C")
    elif 70 <= grade <73:
        print("Your Grade is = C-")
    elif 67 <= grade <70:
        print("Your Grade is = D+")
    elif 63 <= grade <67:
        print("Your Grade is = D")
    elif 60 <= grade <63:
        print("Your Grade is = D-")
    elif grade < 60:
        print("Your Grade is = F")

print("The Average Score is:", grade)
    
        
