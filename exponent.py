# Iterative exponent

def exponent(a,b):
    result = 1
    number = 0
    for i in range (0,b):
        if number is not b:
            result = result*a
            number += 1
            # print 'result', result
            # shorter syntax: result*=a
            # print 'number', number
        else: print 'done'
    return result


def exp1(a,b):
    ans = 1
    while (b>0):
        ans *= a
        b -= 1
    return ans

def exp2(a,b):
    if b==1:
        return a
    else: return a*exp2(a,b-1)

def exp3(a,b):
    if b==1:
        return a
    if (b%2)*2 ==b:
        return exp3(a*a, b/2)
    else: return a*exp3(a,b-1)

def g(n,m):
    x = 0
    for i in range(n):
        for j in range(m):
            x += 1
    return x

def Tower(size, fromStack, toStack, spareStack):
    if size == 1:
        print 'Move disk from ', fromStack, 'to ', toStack
    else :
        Tower(size-1,fromStack,spareStack,toStack)
        Tower(1,fromStack,toStack,spareStack)
        Tower(size-1,spareStack,toStack,fromStack)
