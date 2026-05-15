""" 
Implement a program that reads in the following details pertaining to a list of assignments that a
student is required to complete during a semester, assuming that all assignments are given at the
beginning of the semester:
1) Module name
2) Number of credits for module
3) Deadline of assignment (week number between 1 and 10 inclusive)
4) Maximum mark (in terms of percentage of the coursework mark)
Your program then sorts the assignments in the order they must be done based on the following
criteria (in order of priority):
1) Deadline of assignment
2) Maximum mark
3) Number of credits for module
Your program must display the sorted list of assignments.
"""


def input_assignment(index):
	print(f"Enter details for assignment {index}:")
	moduleName = input("Module name: ")
	credits = int(input("Number of credits: "))
	deadline = int(input("Deadline week (1-10): "))
	maximumMark = float(input("Maximum mark (%): "))
	return {
		"moduleName": moduleName,
		"credits": credits,
		"deadline": deadline,
		"maximumMark": maximumMark,
	}


def sort_assignments(assignments):
	return sorted(assignments, key=lambda assignment: (assignment["deadline"], assignment["maximumMark"], assignment["credits"]))


def display_assignments(assignments):
	print("\nSorted assignments:")
	for assignment in assignments:
		print(
			f"{assignment['moduleName']} | Credits: {assignment['credits']} | "
			f"Deadline: {assignment['deadline']} | Maximum mark: {assignment['maximumMark']}"
		)


def main():
	numberOfAssignments = int(input("Enter the number of assignments: "))
	assignments = []

	for index in range(1, numberOfAssignments + 1):
		assignments.append(input_assignment(index))

	sortedAssignments = sort_assignments(assignments)
	display_assignments(sortedAssignments)


if __name__ == "__main__":
	main()