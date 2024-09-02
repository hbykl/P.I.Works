def isPrimeNumber(i, j=2):
    if i <= 2:
        return True if i == 2 else False
    if i % j == 0:
        return False
    if j * j > i:
        return True
    return isPrimeNumber(i, j + 1)

def findPrimeNumber(first, last):
    if first > last:
        return
    if isPrimeNumber(first):
        print(first)
    findPrimeNumber(first + 1, last)

findPrimeNumber(500, 600)