# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

stu_heights = 0

# print(s_heights)
for s_heights in student_heights:
    stu_heights += s_heights


count = 0
for s_heights in student_heights:
    count = count + 1
# print(count)

Average = stu_heights / count
print(round(Average))
    

