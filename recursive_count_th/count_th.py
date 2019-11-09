count = 0


def count_th(word):
    global count
    if len(word) == 0:
        return count
    if word[:2] == "th":
        count = count + 1
        word = word[2:]
        count_th(word)
    elif word[:2] != "th":
        if word[1:3] == "th":
            count = count + 1
            word = word[2:]
            count_th(word)
        elif word[1:3] != "th":
            word = word[2:]
            count = count
            count_th(word)
    return count


print(count_th("THtHThth"))
