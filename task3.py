x = input("Enter your list of words, separated by white space: ")
list_of_words = x.lower().split()

d = {}
length = len(list_of_words)

y = 0

for i in range(length):

    if list_of_words[i] not in d:

        for j in range(i, length):

            if list_of_words[i] == list_of_words[j]:
                y += 1

        d[list_of_words[i]] = y
        y = 0

print(d)