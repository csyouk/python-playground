import itertools

def dcc(string):
    L = slicing(string)
    for index in L:
        print index
    return L



def slicing(string):
    index = 0
    L=[]
    for letter in string:
        L.append(letter)
    return L


mylist = [1,2,3,4,5]

for i in range(len(mylist)):
    for j in range(i+1, len(mylist)):
        compare(mylist[i],mylist[j])
        print mylist[i], mylist[j]
