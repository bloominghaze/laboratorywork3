sentence = input("Введіть речення: ")

words = sentence.split()

words_starting_with_yak = [word for word in words if word.lower().startswith("як")]

if words_starting_with_yak:
    print("Слова, які починаються на 'як':")
    for word in words_starting_with_yak:
        print(word)
else:
    print("Слів, які починаються на 'як', не знайдено.")
