import threading

def Small_letters(String):
    lowercase = []
    count = 0
    for i in range(len(String)):
        if(String[i]>='a' and String[i]<='z'):
            lowercase.append(String[i])
            count = count+1
    print("Thread ID of Small_letters thread is: ",threading.get_ident())
    print("Thread Name of Small_letters thread is: ",threading.current_thread().name)
    print("Small characters are: ", lowercase)
    print("count of Small characters are: ", count)

def Capital_letters(String):
    Uppercase = []
    count = 0
    for i in range(len(String)):
        if(String[i]>='A' and String[i]<='Z'):
            Uppercase.append(String[i])
            count = count+1
    print("Thread ID of capital_letters thread is: ",threading.get_ident())
    print("Thread Name of Capital_letters thread is: ",threading.current_thread().name)
    print("Capital characters are: ", Uppercase)
    print("count of Capital characters are: ", count)

def Digits_letters(String):
    Integer = []
    count = 0
    for i in range(len(String)):
        if(String[i]>='0' and String[i]<='9'):
            Integer.append(String[i])
            count = count+1
    print("Thread ID of Digit_letters thread is: ",threading.get_ident())
    print("Thread Name of Digits_letters thread is: ",threading.current_thread().name)
    print("Digits are: ", Integer)
    print("count of Digits are: ", count)


def main():
    Small = threading.Thread(target = Small_letters, args=("ArVgTe122323",))
    Capital = threading.Thread(target = Capital_letters, args=("ArVgTe122323",))
    Digit = threading.Thread(target = Digits_letters, args=("ArVgTe122323",))
    Small.start()
    Small.join()
    print("-"*30)

    Capital.start()
    Capital.join()
    print("-"*30)

    Digit.start()
    Digit.join()
    print("-"*30)
    
    print("End of main")

if __name__ == "__main__":
    main()

    