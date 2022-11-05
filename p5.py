def check_prime(num):
    if num==0 or num==1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

n=int(input())
num_primes=0

for i in range(2, n+1):
    if check_prime(i):
        num_primes+=1

print(num_primes)
