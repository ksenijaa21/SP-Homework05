char = ["c", "a", "t", "d", "o", "g"]
new_str = ""


for i in range(len(char)):
    for j in range(len(char)):
        for m in range(len(char)):
            for n in range(len(char)):
                for p in range(len(char)):
                    for q in range(len(char)):
                        if (i != j and i != m and i != n and i != p and i != q
                                and j != m and j != n and j != p and j != q and m != n
                                and m != p and m != q and n != p and n != q and p != q):

                            new_str += char[i] + char[j] + char[m] + char[n] + char[p] + char[q] + "\n"

print(new_str)
