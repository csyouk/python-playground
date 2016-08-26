def test_var_args(farg, *args):
    print("formal arg:", farg)
    print(type(args))
    for arg in args:
        print("another arg:", arg)

test_var_args(1, "two", 3)
print("="*10)
def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    print(kwargs)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))

test_var_kwargs(farg=1, myarg2="two", myarg3=3)


def test_v_kw(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

d = {"arg3":3, "arg2":33}
test_v_kw(3234, **d )