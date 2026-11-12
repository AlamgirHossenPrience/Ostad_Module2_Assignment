name = input("Enter your name: ")
bangla = int(input("Enter Bangla mark: "))
english = int(input("Enter English mark: "))
math = int(input("Enter Math mark: "))

total_mark = bangla + english + math

average_mark = total_mark / 3

if average_mark >= 80 and average_mark <= 100:
  final_grade = "A+"
elif average_mark >= 70 and average_mark <= 79:
  final_grade = "A"
elif average_mark >= 60 and average_mark <= 69:
  final_grade = "B"
elif average_mark >= 50 and average_mark <= 59:
  final_grade = "C"
elif average_mark >= 0 and average_mark < 50:
  final_grade = "F"
else:
  final_grade = ":("

print()
print(f"Student Name: {name}")
print(f"Total Marks: {total_mark}")
print(f"Average Mark: {f"{average_mark: .2f}"}")
print(f"Grade: {final_grade}")

