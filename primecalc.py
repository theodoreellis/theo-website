#prime factorization algorithm

def prime_calc(x):
#input the number to be factored as x
    #use orig_x to clean up list at end
    #orig_x = x
    #seed the list with 2 and 3
    #primes = [2,3]
    primes = []
    #check whether existing primes can factor the number
    while x % 2 == 0:
        x = (x / 2)
        primes.append(2)
    while x % 3 == 0:
        x = (x / 3)
        primes.append(3)

    #for prime in primes:
    #    while x % prime == 0:
    #        x = x / prime
    #create 'candidate primes' by adding 2 to the highest existing prime
    #candidate_prime = max(primes)+2
    cp = 5

    #so long as number has not been fully factored (i.e. divided down to 1, test new candidate primes)
    while x > 1:
        if x % cp == 0:
            x = x / cp
            #when a number factors the number, it is added to the list of primes
            primes.append(cp)
        else:
            cp = cp+2

    #remove the seeded 2 and 3 if they are not actually prime factors
    #if orig_x % 2 != 0:
    #    primes.remove(2)
    #if orig_x % 3 != 0:
    #    primes.remove(3)
    return primes
#code to test
#x = int(input('>'))
#primes = prime_calc(x)
#print(primes)
