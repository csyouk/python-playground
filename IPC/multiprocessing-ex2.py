from multiprocessing import Process, Lock

def f(arg):
    assert False, "ok"
    print("arg", arg)

if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        Process(target=f, args=(lock,)).start()

