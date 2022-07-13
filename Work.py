
def verifIfIsWord(word):
    f = open("work.txt", mode='r', encoding='utf-8')
    result = f.read().find(word)
    f.close()
    return result
