from string import ascii_uppercase

alphabet_dict = {x: i for i, x in enumerate(ascii_uppercase, 1)}  # generate alphabet with values

def tri_numbers(n):

    tri_number_list = list()

    for i in range(1, n + 1):
        tri_number_list.append(int(0.5 * i * (i + 1)))

    return tri_number_list

def word_value(word):

    letter_number = list()

    for letter in word:
        letter_number.append(alphabet_dict[letter])

    return sum(letter_number)

def tri_word_checker(word):

    if word_value(word) in tri_numbers(10000):
        print word, "is a triangle word"
        return True
    else:
        return None

file_words = open('p042_words.txt', 'r')
count = 0
words_list = list()

file_words.split()

for word in file_words:
    words_list.append(word)

print words_list















