s = input("Введіть довільний рядок: ")

letters_only = [char for char in s if char.isalpha()]

half_length = len(letters_only) // 2

result = ''
letter_count = 0

for char in s:
    if char.isalpha():
        if letter_count < half_length:
            result += char
            letter_count += 1
        else:
            break
    else:
        result += char

print(f"Половина рядка: {result}")
