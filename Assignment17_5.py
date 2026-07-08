def Prime_number(a):
    x=0
    for i in range(2,a):
        if(a%i==0):
            x = x+1
    if(x>0):
        print("Not prime")
    else:
        print("Prime")

Prime_number(13)     
