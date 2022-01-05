# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student score ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_score = sum(student_scores)
number_of_students = len(student_scores)
average_score = total_score / number_of_students
print(round(average_score))