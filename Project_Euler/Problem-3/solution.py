from math import sqrt 

def is_prime(n): 
    for a in range(2, int(sqrt(n))): 
        if n % a == 0: 
            return False 
    return True 

def prime_factors(x): 
    my_list = [] 
    for no3 in range(2, int(sqrt(x))): 
        if x % no3 == 0: 
            # no3 and x/no3 are factors of x 
            if is_prime(no3): 
                my_list.append(no3) 
            if is_prime(x/no3): 
                my_list.append(no3) 
    print(max(my_list)) 
