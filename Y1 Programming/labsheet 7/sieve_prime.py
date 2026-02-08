def main():
    primes = list(range(2, 1 + int(input('enter a positive integer: '))))
    print(primes)
    i = 0
    while (i < len(primes)):
        print("i:",i, "num:", primes[i])
        if (primes[i] == None):
            del primes[i]
        else:
            for k in range(i + primes[i], len(primes), primes[i]):
                primes[k] = None
            i += 1
        print(primes)
# main()
