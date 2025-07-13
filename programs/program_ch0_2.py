import math

def generate_primes(n):
    prime_list = []
    for i in range(n):
        if i == 0:
            prime_list.append(2)
        else:
            p=prime_list[i-1]+1
            sqrtp = math.sqrt(p)
            j = 0
            while prime_list[j] <= sqrtp:
                if p%prime_list[j] == 0:
                    p = p+1
                    sqrtp = math.sqrt(p)
                    j = -1
                j = j+1
            prime_list.append(p)
    return prime_list

def prime_decomposition(number,prime_list):
    if int(number) != number:
        print(f"{number} is not an integer")
    temp_number = number
    decomp_list = []
    n = len(prime_list)
    for i in range(n):
        decomp_list.append(0)
        while temp_number%prime_list[i]==0:
            decomp_list[i] = decomp_list[i]+1
            temp_number = temp_number/prime_list[i]
    return decomp_list

def prime_construction(prime_list, decomp_list):
    number = 1
    for i in range(len(decomp_list)):
        number = number * prime_list[i] ** decomp_list[i]
    return number
    
prime_list = generate_primes(25)
print(prime_list)
d_l = prime_decomposition(36, prime_list)
print(d_l)
con = prime_construction(prime_list, d_l)
print(con)