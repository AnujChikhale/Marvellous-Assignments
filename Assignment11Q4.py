def Reverse(a):
    reverse = 0
    while(a>0):
        digit = a%10
        reverse = reverse*10+digit
        a = a//10
    return reverse

print(Reverse(473232))  #output = 232374