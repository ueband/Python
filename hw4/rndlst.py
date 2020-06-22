from random import randint

def newlst(n = 10, rng = 100):
    lst = []
    for i in range(n):
        lst.append(randint(0,rng))
    return lst

if __name__ == '__main__':
    print(newlst())