check = False;lesson_list = [] ; try_signIn = 3 
name = "muhammet mustafa doğan"
results = {"midterm":38,"final":66,"project":89}
def calculateGrade():
    mean = (results["midterm"]*30 + results["final"]*50 + results["project"]*20)/100
    return mean

while range(3):
    user = input("Please enter your name: ")
    if user.lower() == name:
        print(f"Welcome {user.upper()}")
        for i in range(5):
            ask = input("Press q for complete or enter any key to continue : ")
            i += 1
            if ask == "q":
                break
            lessons = input(f"Please choose lesson {i} : ")
            lesson_list.append(lessons)
            check = True
    
        break
    else:
        try_signIn -= 1
        if try_signIn == 0:
            print("Plese try again later.")
            break
if len(lesson_list) < 3:
    print("You are failed in class.")

if check == True:
    print("".center(20,"-"))
    print("Please select lesson for calculate your grade")
    print(f"Your lessons\n1-{lesson_list[0]}\n2-{lesson_list[1]}\n3-{lesson_list[2]}\n4-{lesson_list[3]}\n5-{lesson_list[4]}")
    lessonNum = int(input("Choose your lesson number:"))
    while True:    
        if lessonNum < 1 and lessonNum > 5:
            print("You must enter number of list")
        else:
            grade = calculateGrade()
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
        