text = input("Введіть 2 слова: ")
text1 = text.split()
if len(text1) >= 2:
    print(text[::-1])
    print(' '.join(text1[::-1]))
else:
    print("Рядок не містить мінімум 2 слова. Спробуйте ще раз.")