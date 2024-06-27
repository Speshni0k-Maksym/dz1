# Завдання 1
n = input("Введіть слово паліндромом: ")
if n==n[::-1]:
    print(n)
else:
    print("Це не слово паліндромом")
# Завдання 2
text = "This is my Python code"
print(text)
text1 = input("Введіть букву яку хочете перерахувати в цьому рядку: ")
if len(text1) != 1:
    print("Будь ласка, введіть лише одну букву.")
else:
    count = 0
    b = text.find(text1)
    
    while b != -1:
        count += 1
        b = text.find(text1, b + 1)
    
    print(f"Буква '{text1}' зустрічається у рядку {count} разів.")
# Завдання 3
text2 = input("Введіть 2 слова: ")
text3 = text2.split()
if len(text3) >= 2:
    print(text2[::-1])
    print(' '.join(text3[::-1]))
else:
    print("Рядок не містить мінімум 2 слова. Спробуйте ще раз.")