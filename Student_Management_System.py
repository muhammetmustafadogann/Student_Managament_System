check = False;lesson_list = [] ; try_signIn = 3 
name = "Muhammet Mustafa Doğan"
def calculateGrade():
    d = {}
    keys= ["midterm","final","project"]
    for i in range(len(keys)):
        values = int(input(f"Enter {keys[i]} note: ")) 
        key = keys[i]
        d[key] = values
    print('-'*20)
    mean = (d["midterm"]*30 + d["final"]*50 + d["project"]*20)/100
    return mean
def lesson_check():
    if len(lesson_list) < 3:
        return "You are failed in class."
while range(3):
    user = input("Please enter your name: ")
    if user.lower() == name.lower():
        print(f"Welcome {user.upper()}")
        print("Press q for complete after choosing lessons.")
        for i in range(5):
            i += 1
            lessons = input(f"Please addding lesson(s) {i} : ")
            if lessons == "q":
                print(lesson_check())
                break 
            lesson_list.append(lessons)
        check = True
        break
    else:
        try_signIn -= 1
        if try_signIn == 0:
            print("Plese try again later.")
            break
if check == True:
    print("".center(20,"-"))
    print("Please select lesson for calculate your grade\nYour lessons")
    for i in range(len(lesson_list)):
        print(f"{i+1}-{lesson_list[i]}")
    while True:
        lessonNum = int(input("Choose your lesson number:"))
        print('-'*20)
        if lessonNum > len(lesson_list) or lessonNum <= 0:
            print(f"You have {len(lesson_list)} lessons.Please enter a valid number.")
        else:
            break
    while True:    
        if lessonNum < 1 and lessonNum > 5:
            print("You must enter number of list")
        else:
            grade = calculateGrade()
            print('-'*20)
            if grade >= 90:
                print(f"Your grade is {grade}:AA ")
            elif grade >= 70 and grade < 90:
                print(f"Your grade is {grade}:BB ")
            elif grade >= 50 and grade < 70:
                print(f"Your grade is {grade}:CC ")    
            elif grade >= 30 and grade < 50:
                print(f"Your grade is {grade}:DD ")
            elif grade < 30:
                print(f"Your grade is {grade}:FF\nYou did not pass this lesson.")
        break
