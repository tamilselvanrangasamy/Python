def check_prime(num):
    if(num<2):
        print("The number  is not Prime ")
        return
    for i in range(2,num//2):
        if(num%i==0):
            print("The number is not prime")
            return
    print("The number is prime")
num=int(input("Enter num: "))
check_prime(num)
