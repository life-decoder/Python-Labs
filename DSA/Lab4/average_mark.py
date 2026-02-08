numStudent = 3
studentMark = []

# read the marks for numStudent students
for i in range(numStudent):
    studentMark.append(eval(input("Please enter mark for student " + str(i + 1) + ":")))

# calculate the average mark
averageMark = sum(studentMark)/numStudent

# print the average mark
print("Average mark: ", round(averageMark,2))
