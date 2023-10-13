number1 = 101
number2 = 64

product1 = number1 * number2
sum1 = number1 + number2

print("First set: (101 and 64):")
print("Product:", product1)
print("Sum:", sum1)

number3 = 3.50
number4 = -5
number5 = 13.1111

product2 = number3 * number4 * number5
sum2 = number3 + number4 + number5

print("\nSecond set: (3.50, -5, and 13.1111):")
print("Product:", product2)
print("Sum:", sum2)

number6 = -55.13
number7 = 23

product3 = number6 * number7
sum3 = number6 + number7

print("\nThird set: (-55.13 and 23):")
print("Product:", product3)
print("Sum:", sum3)

students = {
    "Ali B.": {"Physics": 80, "Math": 90},
    "Aisha G.": {"Physics": 78, "Math": 89},
    "Nur D.": {"Physics": 60, "Math": 76},
    "Mehmet C.": {"Physics": 100, "Math": 84},
    "Usama H.": {"Physics": 98, "Math": 90},
    "Hamza K.": {"Physics": 70, "Math": 80},
    "Farouk T.": {"Physics": 67, "Math": 73},
    "Deniz A.": {"Physics": 99, "Math": 91},
    "Yasmine R.": {"Physics": 87, "Math": 100},
    "Ahmet S.": {"Physics": 93, "Math": 91}
}

student_name = input("\nEnter student's name: ")

if student_name in students:
    grades = students[student_name]
    print("Grades for " + student_name + ":")
    for subject in grades:
        grade = grades[subject]
        print(subject + ": " + str(grade) + "/100")
else:
    print("Error! No student found with this name.")