statement = raw_input('Typing the statement : ')

def inverse(arg):
    temp_list = []
    initial_number = 1
    for i in arg:
        print 'this', i
        temp_list.append(arg[-initial_number])
        initial_number += 1
    print "".join(temp_list)
