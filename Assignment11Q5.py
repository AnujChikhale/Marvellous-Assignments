def Palindrome(a):
    original = a
    reverse = 0
    while(a>0):
        digit = a%10
        reverse = reverse*10+digit
        a = a//10
    if(original == reverse):
        print("Number is palindrome")
    else:
        print("Number is not palindrome")

Palindrome(424)