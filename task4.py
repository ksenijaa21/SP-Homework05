import matplotlib.pyplot as plt


x = input("Your document: ")


d = {}
length = len(x)


for i in range(length):

    if x[i] not in d and x[i].isalpha():

        y = 0

        for j in range(i, length):

            if x[i] == x[j]:
                y += 1

        d[x[i]] = y


plt.bar(range(len(d)), list(d.values()), align='center')
plt.xticks(range(len(d)), list(d.keys()))

plt.show()