# make combinations by combining all words in list below
words = {"instagram", "handle", "examples", "here"}

with open("wordlist.txt", "w") as wordstext:
    for w in words:
        for w2 in words:
            if w != w2:
                wordstext.write(w + w2 + "\n")