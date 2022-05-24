# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
total = 0
for s in word.lower():
    
    if s in ('а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я'):
        total += 1
    
print(total)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
print(len(words))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for s in words:
    print(s[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
all_len = 0
for s in words:
    all_len += len(s)
print(all_len/len(words))
