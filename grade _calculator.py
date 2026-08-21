# Student Grade Calculator

name = input("Enter Student Name: ")

marks = []  # Created a list
subjects = ["Bangla", "English", "Math", "Physics", "Chemistry"]
for sub in subjects:
    m = int(input(f"Enter marks for {sub}: "))
    marks.append(m)
total = sum(marks)
average = total / 5
percentage = (total / 500) * 100  # Added percentage

print("\n------ Result ------")
print("Total Marks:", total)
print("Average:", average)
percentage = (total/500)*100
print("Percentage:", percentage, "%")
