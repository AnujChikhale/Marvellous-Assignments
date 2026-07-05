digit = lambda x : x%2==0

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    count = 0

    ret = list(filter(digit, Data))
    count = 0
    for no in ret:
        count = count+1
        
    print(count)

if __name__ == "__main__":
    main()