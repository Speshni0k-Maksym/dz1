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
