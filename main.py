# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total = 0
length = 0
for height in student_heights:
  total += height
  length += 1
average = total /  length
#Write your code below this row 

print(average)

