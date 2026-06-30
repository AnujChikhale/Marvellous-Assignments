def SumofDigits(a):
    Sum = 0
    while(a>0):
        digit = a%10
        Sum = Sum+digit
        a = a//10
    return Sum

print(SumofDigits(149))
