def is_prime(num):
    if num <=1:
        print("its not prime")
        return

    for i in range(2,num):
        if num %i ==0:
            print("its not prime")
            return
            

    print("prime")

is_prime(10)