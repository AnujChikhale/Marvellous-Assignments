def DigitCount(a):
    count = 0
    if a == 0 :
        count = 1
    else:
        while a>0:
            count = count+1
            a = a//10
    return count

print(DigitCount(123456353))