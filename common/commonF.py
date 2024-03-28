def hc_factor(a: int, b: int) -> int:
    while a!=b:
        if a==b:
            return a
        elif a>b:
            a-=b
        else:
            b-=a
            
    return a