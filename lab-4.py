text = "This is a sample string for testing."
print("Жол ұзындығы", len(text))
print("Бас әріп:", text.upper())
print("Кіші әріп:", text.lower())
print("Бірінші әріп бас әріп:", text.capitalize())
print("Әр сөз бас әріппен жазылады:", text.title())
print("Жол 'This' деп басталады ма?", text.startswith("This"))
print("'Testing' жолымен аяқталады ма?", text.endswith("testing."))
print("'is' ішкі жолы неше рет кездеседі?", text.count("is"))
new_text = text.replace("sample", "new")
print("'sample' дегенді 'new' деп ауыстырыңыз:", new_text)

# words = text.split(" ")
# print("Жолдағы сөздер", words)

#2esep
# students = []
# while True:
#     name = input("Введите фамилию ученика : ")
#     if not name:
#         break
#     grade = int(input("Введите класс ученика: "))
#     students.append((name, grade))# students.sort(key=lambda x: x[1])
# print("Список учеников по возрастанию классов:")
# for student in students:
#     print(f"{student[0]} - {student[1]} класс")

# 3 esep
# string = str(input())
# upper = 0
# lower = 0
# for i in string:
#     if i.isupper():
#         upper += 1
#     else:
#         lower += 1
# if upper > lower:
#     print(string.upper())
# else:
    # print(string.lower())

#4esep
# while True:
#     num1 = input("n1 = ")
#     num2 = input("n2 = ")
#     if num1.isdigit() and num2.isdigit():
#         num1 = int(num1)
#         num2 = int(num2)
#         print(f"Сандардың қосындысы: {num1 + num2}")
#         break
#     else:
#         print("Қате: бүтін сандарды енгізу керек!")