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

def prime_construction(prime_list, decomp_list):
    number = 1
    for i in range(len(decomp_list)):
        number = number * prime_list[i] ** decomp_list[i]
    return number

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
    if prime_construction(prime_list,decomp_list) != number:
        print(f"not enough primes to represent {number}")
    else:
        return decomp_list

def gcd(a,b,prime_list):
    pd_a = prime_decomposition(a,prime_list)
    pd_b = prime_decomposition(b,prime_list)
    gcd_list = []
    for i in range(len(prime_list)):
        gcd_list.append(min(pd_a[i],pd_b[i]))
    gcd = prime_construction(prime_list, gcd_list)
    return gcd
    
def lcm(a,b,prime_list):
    pd_a = prime_decomposition(a,prime_list)
    pd_b = prime_decomposition(b,prime_list)
    lcm_list = []
    for i in range(len(prime_list)):
        lcm_list.append(max(pd_a[i],pd_b[i]))
    lcm = prime_construction(prime_list, lcm_list)
    return lcm
    
prime_list = generate_primes(1000)
print(prime_list)
# d_l = prime_decomposition(36, prime_list)
# print(d_l)
# con = prime_construction(prime_list, d_l)
# print(con)

print("\n\nChapter 0.2 - EXERCISE 1:")
def gcd_lcm(a,b,prime_list):
    g = gcd(a,b,prime_list)
    l = lcm(a,b,prime_list)
    return (g,l)
numbers = [(20,13),(69,372),(792,275),(11391,5673),(1761,1567),(507885,60808)]
answers = []
for i in range(len(numbers)):
    answers.append(gcd_lcm(numbers[i][0],numbers[i][1],prime_list))
print(answers)