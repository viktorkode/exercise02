def evenwords(str1: any):
    str2=str1.split(' ')
    words=[zbor for zbor in str2 if len(zbor) % 2 == 0]
    return " ".join(words)